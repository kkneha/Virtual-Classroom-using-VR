var scene = document.querySelector('#scene');
//var x = {{ obj_no }};
console.log(x)
function create_abox(){
     var box = document.createElement('a-box');
     box.setAttribute(
         'color', 'blue'    
     )
     box.setAttribute(
         'position', '-1 0.5 -2'
     )
     return box;
 }

function create_asphere(){
    var sphere = document.createElement('a-sphere');
    sphere.setAttribute(
        'color', 'blue'
    )
    sphere.setAttribute(
        'position', '0 1.25 -5'
    )
    sphere.setAttribute(
        'radius', '1.25'
    )
    return sphere;
}

function create_acylinder(){
    var cylinder = document.createElement('a-cylinder');
    cylinder.setAttribute(
        'color', 'blue'
    )
    cylinder.setAttribute(
        'position', '-1 0.5 -2'
    )
    cylinder.setAttribute(
        'radius', '0.5'
    )
    cylinder.setAttribute(
        'height','1.5'
    )
    return cylinder;
}

var obj;
switch(x)
{ 
    case 0:
        obj = create_abox()
        break;
    case 1:
        obj = create_asphere()
        break;
    case 2:
        obj = create_acylinder()
        break;
}
scene.appendChild(obj) 

/* setTimeout(() =>{
    var box = create_abox();
    scene.appendChild(box);
 }, 2000); */