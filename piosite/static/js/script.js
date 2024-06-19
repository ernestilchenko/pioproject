'use strict';
const ink = document.getElementById('exampleInputEmail1');
console.log(ink.value);
ink.addEventListener('click', eve => {
    eve.target.select();
});