
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
   }
 
   // Main root component
   class Root extends Component {
     static template = "Root"
     static components = { Card, Counter, Char };
     
     setup() {
       this.state = useState({a: 1, b: 3, data:[1,2,3,4], data2:[8,9,15,31]});
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
 