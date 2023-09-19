import "./style.scss";

import Sliderm from "sliderm";
import "sliderm/src/assets/scss/index.scss";

const sliderm = new Sliderm('#main-slider', {
    arrow: true,
    pagination: true,
    grouping: false,
    loop: true,
    preview: false,
    columns: 1,
    duration: 300,
    spacing: 10,
    autoplay: true,
    align: 'center',
});