
/**
 * This is the javascript code defined in the playground.
 * In a larger application, this code should probably be moved in different
 * sub files.
 */
import * as utils from "./utils.js";
//  async function app(TEMPLATES) {


// We show here how slots can be used to create generic components.
// In this example, the Card component is basically only a container. It is not
// aware of its content. It just knows where it should be (with t-slot).
// The parent component define the content with t-set-slot.
//
// Note that the t-on-click event, defined in the Root template, is executed in
// the context of the Root component, even though it is inside the Card component
const { Component, useState, mount } = owl;

class Card extends Component {
    static template = "Card";
    
    setup() {
    this.state = useState({ showContent: true });
    }

    toggleDisplay() {
    this.state.showContent = !this.state.showContent;
    }
}

class Counter extends Component {
    static template = "Counter";
    
    setup() {
    this.state = useState({val: 1});
    }

    inc() {
    this.state.val++;
    }
}

class LedRow extends Component {
    static template = "LedRow"
}


class Char extends Component {
    static template = "Char"
    static components = { LedRow };
}

// Main root component
class Root extends Component {
    static template = "Root"
    static components = { Card, Counter, Char };
    
    setup() {
        this.state = useState({
            a: 1, b: 3, 
            data:[1,2,3,4], data2:[8,9,15,31],
            planes: [
                // [0, 0, 0, 14, 10, 14, 2, 14],
                // [1, 1, 1, 1, 29, 23, 16, 31]
                [],
                [],
                [],
                [],
                [],
                [0, 0, 16, 31, 17, 31, 0, 0],
                [1, 1, 1, 1, 29, 23, 16, 31],
                [],
                [17, 25, 1, 21, 21, 21, 29, 0],
                [0, 0, 0, 1, 7, 5, 7, 0],
                [],
                [0, 0, 0, 14, 8, 31, 0, 0],
                [1, 1, 1, 1, 29, 23, 16, 31],
                [],
                [28, 20, 28, 16, 28, 4, 28, 0],
                [5, 5, 7, 4, 7, 5, 7, 0],
                [],
                [],
                [],
                [],
                
                //? basmalah-sentence
                [],
                [],
                [0, 0, 0, 4, 4, 28, 0, 8],
                [0, 0, 1, 21, 21, 31, 0, 0],
                [0, 0, 0, 28, 20, 31, 16, 16],
                // [0, 0, 0, 0, 14, 27, 14, 0],
                [],
                [17, 25, 1, 21, 21, 21, 29, 0],
                [0, 0, 0, 1, 7, 5, 7, 0],
                [],
                [10, 10, 10, 10, 10, 26, 0, 0],
                [0, 0, 0, 0, 1, 2, 18, 12],
                [12, 18, 2, 4, 2, 31, 0, 0],
                [0, 0, 0, 0, 14, 27, 14, 0],
                [0, 0, 0, 4, 17, 17, 31, 0],
                [],
                [10, 10, 10, 10, 10, 26, 0, 0],
                [0, 0, 0, 0, 1, 2, 18, 12],
                [12, 18, 2, 4, 2, 31, 0, 0],
                [0, 0, 0, 29, 21, 31, 16, 21],
                [],
                [],

                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                
                [],
                [],
                [0, 0, 0, 1, 31, 0, 4, 0],
                [0, 0, 21, 21, 31, 0, 0, 0],
                [0, 0, 0, 14, 11, 30, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],

                [10, 10, 10, 10, 26, 0, 0, 0],
                [5, 5, 29, 21, 31, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],

                [5, 5, 5, 5, 13, 8, 8, 24],
                [12, 18, 2, 2, 31, 0, 0, 0],
                [0, 0, 0, 14, 11, 30, 0, 0],
                [0, 0, 4, 17, 17, 31, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],

                [5, 5, 5, 5, 13, 8, 8, 24],
                [12, 18, 2, 2, 31, 0, 0, 0],
                [0, 0, 28, 21, 31, 16, 21, 16],
                [],
                [],
                [],
                

                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],

                                
                [],
                [],
                [0, 0, 0, 1, 31, 0, 4, 0],
                [0, 0, 21, 21, 31, 0, 0, 0],
                [0, 0, 0, 14, 11, 30, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],

                [10, 10, 10, 10, 26, 0, 0, 0],
                [5, 5, 29, 21, 31, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],

                [10, 10, 10, 10, 26, 0, 0, 0],
                [8, 20, 4, 5, 29, 1, 1, 6],
                [0, 0, 0, 14, 11, 30, 0, 0],
                [0, 0, 4, 17, 17, 31, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                
                [10, 10, 10, 10, 26, 0, 0, 0],
                [8, 20, 4, 5, 29, 1, 1, 6],
                [0, 0, 28, 21, 31, 16, 21, 16],
                [],
                [],
                [],
                

                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                
            ]
        });
    }

    inc(key, delta) {
    this.state[key] += delta;
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
        templates = await owl.loadFile('/app.xml');
    } catch(e) {
        console.error(`This app requires a static server.  If you have python installed, try 'python app.py'`);
        return;
        }
        prepareOWLApp(templates);
        mount(Root, document.body, { templates: templates, dev: true});
    //    app(templates);
}
    
start();
    