import React, { Component } from 'react';
import {BrowserRouter as Router, Route } from './react-router-dom.min.js'

import logo from '../img/logo.svg';
import '../css/App.css';

import _ from "lodash";
import ListItem from './ListItem.jsx';

import Home from

class DocumentList extends Component {
  constructor(props) {
    super(props);

    this.state = {
      chores: [
        {
          id: 1,
          name: "Take out trash",
          description: "Trash removal from both bins",
          completed: true
        },
        {
          id: 2,
          name: "Do the Dishes",
          description: "Wash and dry the dishes",
          completed: false
        },

      ]
    };
  }

  handleOnClick = id => {
    const chores = _.cloneDeep(this.state.chores);

    for (let chore of chores) {
      if (chore.id === id) {
        chore.completed = !chore.completed;
        break;
      }
    }

    this.setState({ chores });
  };

//  render() {
//    const { chores } = this.state;
//    return (
//      <div className="App">
//        <h1>Chores</h1>
//        <ul>
//          {chores.map(chore => (
//            <ListItem
//              key={chore.id}
//              id={chore.id}
//              name={chore.name}
//              completed={chore.completed}
//              description={chore.description}
//              handleOnClick={this.handleOnClick}
//            />
//          ))}
//        </ul>
//      </div>
//    );
//  }
    render(){
        return ( <h1> hey </h1> )
        //return( <Router> <div> <Route exact path="/" component= { Home } /> </div> </Router>);
    }
}

//export default App;
export default DocumentList;

