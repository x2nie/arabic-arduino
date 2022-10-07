
/**
 * This is the javascript code defined in the playground.
 * In a larger application, this code should probably be moved in different
 * sub files.
 */
import * as utils from "../utils.js";
//  async function app(TEMPLATES) {


// We show here how slots can be used to create generic components.
// In this example, the Card component is basically only a container. It is not
// aware of its content. It just knows where it should be (with t-slot).
// The parent component define the content with t-set-slot.
//
// Note that the t-on-click event, defined in the Root template, is executed in
// the context of the Root component, even though it is inside the Card component
// source: https://codepen.io/codefoxx/pen/rNmGMbB
const { Component, useState, mount,onWillDestroy, xml } = owl;

const env = {
    grid : {
        left: 261,
        top: 251,
        charsH: 15,
        charsV: 3,
    },
    char: {
        ledH:5,
        ledV:8,
        gapH: 15,
        gapV: 9,
    },
    led: {
        width  :7,
        height :7,
        gapH   :1,
        gapV   :1,
    },
    // dots: {
    //     cols:5,
    //     rows:8,        
    // }
};

// We define here a custom behaviour: this hook tracks the state of the mouse
// position
function useMouse() {
    const position = useState({x:0, y: 0});

    function update(e) {
      position.x = e.clientX;
      position.y = e.clientY;
    }
    window.addEventListener('mousemove', update);
    onWillDestroy(() => {
        window.removeEventListener('mousemove', update);
    });

    return position;
}


class DndImage extends Component {
    static template = xml /* xml */`
        <div t-name="DndImage" 
            class="image_drop_area"
            t-on-dragover="onDragover"
            t-on-drop="onDrop"
            t-attf-style="background:#{state.background};"
        >
            <img t-att-src="state.img_src" alt="preview" />
        </div>
    `;
    
    setup() {
        this.state = useState({ 
            showContent: true, 
            fileName: null,
            background: 'yellow',
            width: '200px',
            height: '200px',
            // img_src: 'data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==',
            img_src: 'sample.png',
        });
    }

    onDragover(event){ // Event listener for dragging the image over the div
        event.stopPropagation();
        event.preventDefault();
        // Style the drag-and-drop as a "copy file" operation.
        event.dataTransfer.dropEffect = 'copy';
    }

    onDrop(event){
        event.stopPropagation();
        event.preventDefault();
        const fileList = event.dataTransfer.files;

        // document.querySelector("#file_name").textContent = fileList[0].name;
        this.fileName = fileList[0].name;
        
        this.readImage(fileList[0]);
    }

    // Converts the image into a data URI
    readImage(file){
        const reader = new FileReader();
        const self = this;
        reader.addEventListener('load', (event) => {
            // const uploaded_image = event.target.result;
            // document.querySelector("#image_drop_area").style.backgroundImage = `url(${uploaded_image})`;
            this.state.img_src = event.target.result;
            // this.state.img_src = `url(${uploaded_image})`;
            // var img = document.createElement('img');
            // img.src = this.state.background;
            // this.state.width = `${img.width}px`;
        });
        reader.readAsDataURL(file);
    }

    toggleDisplay() {
    this.state.showContent = !this.state.showContent;
    }
}


class Char extends Component {
    static template = "Char"
    setup() {
        // this.grid = useState(this.env.grid);
        this.char = useState(this.env.char);
        this.led = useState(this.env.led);
    }
}

class Grid extends Component {
    static template = "Grid"
    static components = { Char };
    setup() {
        this.grid = useState(this.env.grid);
        this.char = useState(this.env.char);
    }
}

// Main root component
class Root extends Component {
    static template = "Root"
    static components = { DndImage, Grid };
    
    setup() {
        this.state = useState({
            zoom: '1.0',
            mousex: 0,
            mousey: 0,
        });

        this.grid = useState(this.env.grid);
        this.char = useState(this.env.char);
        this.led = useState(this.env.led);
        // this.grid = useState({
        //     left: 10,
        //     top: 10,
        //     cols:5,
        //     rows:8,
        // });

        // this hooks is bound to the 'mouse' property.
        // this.mouse = useMouse();
    }

    get zoom_style() {
        const izoom = this.state.zoom;
        return `transform:scale(${izoom});width:${izoom*100}%;`
    }
    zoomed_mousemove(e) {
        this.state.mousex = e.offsetX;
        this.state.mousey = e.offsetY;
    }

}
    
    // Application setup
    //    mount(Root, document.body, { templates: TEMPLATES, dev: true});
    
    // }
    
    /**
     * Initialization code
     * This code load templates, and make sure everything is properly connected.
     */
    function prepareOWLApp(templates) {
        const _configure = owl.App.prototype.configure;
        owl.App.prototype.configure = function configureOverriden(config) {
            config = Object.assign({ dev: true }, config); 
            this.addTemplates(templates);
            return _configure.call(this, config);
        }
    }
    
    async function start() {
        let templates;
        try {
            templates = await owl.loadFile('app.xml');
        } catch(e) {
            console.error(`This app requires a static server.  If you have python installed, try 'python app.py'`);
            return;
        }
        prepareOWLApp(templates);
        mount(Root, document.body, { env, templates: templates, dev: true});
        //    app(templates);
    }
    
start();
    