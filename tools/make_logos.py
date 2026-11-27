import sys,os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
F=sys.argv[1]; OUT=sys.argv[2]; os.makedirs(OUT,exist_ok=True)
med=TTFont(F+'/STIXTwoText-Medium.ttf'); ita=TTFont(F+'/STIXTwoText-Italic.ttf'); reg=TTFont(F+'/STIXTwoText-Regular.ttf')
upm=med['head'].unitsPerEm
def glyph(font,ch): 
    gs=font.getGlyphSet(); n=font.getBestCmap()[ord(ch)]; return gs,n,gs[n].width
def run(font,text,x0,y0,size,track=0.0):
    """returns svg path d, end x; y0 baseline; y flipped"""
    s=size/upm; d=[]; x=x0; bp=None
    for ch in text:
        if ch==' ':
            gs,n,w=glyph(font,' '); x+=w*s+track*size; continue
        gs,n,w=glyph(font,ch)
        pen=SVGPathPen(gs); tp=TransformPen(pen,(s,0,0,-s,x,y0)); gs[n].draw(tp)
        d.append(pen.getCommands()); x+=w*s+track*size
    return ' '.join(d), x
def bounds(font,text,size,track=0):
    gs=font.getGlyphSet(); s=size/upm; x=0; xs=[];ys=[]
    for ch in text:
        n=font.getBestCmap()[ord(ch)]
        bp=BoundsPen(gs); gs[n].draw(bp)
        if bp.bounds: xs+= [x+bp.bounds[0]*s, x+bp.bounds[2]*s]; ys+=[bp.bounds[1]*s,bp.bounds[3]*s]
        x+=gs[n].width*s+track*size
    return min(xs),max(xs),min(ys),max(ys)
# monogram: V (Medium) + f (Italic), tracking -0.04em, as on site nav
S=100
vd,xe=run(med,'V',0,0,S,-0.04)
fd,_=run(ita,'f',xe,0,S,-0.04)
# bounds of combo
b1=bounds(med,'V',S); gsI=ita.getGlyphSet(); bp=BoundsPen(gsI); gsI[ita.getBestCmap()[ord('f')]].draw(bp); fb=bp.bounds; s=S/upm
minx=min(b1[0],xe+fb[0]*s); maxx=max(b1[1],xe+fb[2]*s); miny=min(b1[2],fb[1]*s); maxy=max(b1[3],fb[3]*s)
pad=0
vb=(minx-pad,-maxy-pad,maxx-minx+2*pad,maxy-miny+2*pad)
print('monogram viewBox',[round(v,2) for v in vb])
def svg(vb,body,title='Vertex Fund'):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb[0]:.2f} {vb[1]:.2f} {vb[2]:.2f} {vb[3]:.2f}" role="img" aria-label="{title}"><title>{title}</title>{body}</svg>\n'
COL={'on-light':('#14120E','#A98018'),'on-dark':('#FAFAF8','#D6A72A'),'mono-ink':('#14120E','#14120E'),'mono-paper':('#FAFAF8','#FAFAF8')}
for k,(cv,cf) in COL.items():
    open(f'{OUT}/vf-monogram-{k}.svg','w').write(svg(vb,f'<path fill="{cv}" d="{vd}"/><path fill="{cf}" d="{fd}"/>','Vertex Fund monogram'))
# horizontal lockup: monogram height H; name "Vertex Fund" STIX regular; sub "UNIVERSITY OF MARYLAND" tracked
mh=maxy-miny
gap=0.30*S
nx=maxx+gap
nsize=S*0.42
name1,xe1=run(reg,'Vertex ',nx,-mh*0.40+0,nsize,-0.01)
name2,xe2=run(reg,'Fund',xe1,-mh*0.40,nsize,-0.01)
ssize=S*0.155
sub,xe3=run(reg,'University of Maryland',nx+1,-mh*0.40+ssize*1.75,ssize,0.01)
# remove trailing track
right=max(xe2,xe3-0.01*ssize)
lvb=(minx,-maxy,right-minx,maxy-miny)
for k,(cv,cf) in COL.items():
    sc = {'on-light':'#6E685F','on-dark':'#8C867E'}.get(k,cv)
    body=f'<path fill="{cv}" d="{vd}"/><path fill="{cf}" d="{fd}"/><path fill="{cv}" d="{name1}"/><path fill="{cf}" d="{name2}"/><path fill="{sc}" d="{sub}"/>'
    open(f'{OUT}/vf-lockup-{k}.svg','w').write(svg(lvb,body,'Vertex Fund, University of Maryland'))
# avatar (proposed gold f), 1080 square, ink bg, monogram centered occupying ~52% width (inside circle safe zone)
W=1080; mw=maxx-minx; sc=(W*0.50)/mw; cx=(W-mw*sc)/2 - minx*sc; cy=W/2 + (maxy+miny)/2*sc
body=f'<rect width="{W}" height="{W}" fill="#14120E"/><g transform="translate({cx:.2f} {cy:.2f}) scale({sc:.4f})"><path fill="#FAFAF8" d="{vd}"/><path fill="#D6A72A" d="{fd}"/></g>'
open(f'{OUT}/vf-avatar-ink-1080.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {W}" role="img" aria-label="Vertex Fund"><title>Vertex Fund</title>{body}</svg>\n')
body=f'<rect width="{W}" height="{W}" fill="#FAFAF8"/><g transform="translate({cx:.2f} {cy:.2f}) scale({sc:.4f})"><path fill="#14120E" d="{vd}"/><path fill="#A98018" d="{fd}"/></g>'
open(f'{OUT}/vf-avatar-paper-1080.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {W}" role="img" aria-label="Vertex Fund"><title>Vertex Fund</title>{body}</svg>\n')
# emit raw path data for template embedding
pass
print('ok')
