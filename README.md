# CMP Dataset
CMP [dataset](http://cmp.felk.cvut.cz/~tylecr1/facade/) for facade segmentation.

CMP dataset is assembled at the Center for Machine Perception, which includes 606 rectified images of facades from various sources, which have been manually annotated. The facades are from different cities around the world and diverse architectural styles. Data origin, format and processing, annotation principles for 12 classes are specified below.
<table>
    <tr>
        

<td><img src="https://github.com/wohaiyo/cmp_dataset/blob/master/image/cmp_b0012.jpg" width = 20% height = 20% ></td>
<td><img src="https://github.com/wohaiyo/cmp_dataset/blob/master/label_color/cmp_b0012.png" width = 20% height = 20% ></td>
    </tr>
</table>

## Dataset label (B, G, R)
- 0 background: (170, 0, 0)
- 1 facade: (255, 0 ,0)
- 2 window:(255, 85, 0)
- 3 door: (255, 170, 0)
- 4 cornice: (170, 255, 85)
- 5 sill: (0, 170, 255)
- 6 balcony: (85, 255, 170)
- 7 blind: (0, 255, 255)
- 8 deco: (255, 255, 0)
- 9 molding: (0, 85, 255)
- 10 pillar: (0, 0, 255)
- 11 shop: (0, 0, 170)

## Folder Description

`image`

`label`
