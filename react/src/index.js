import React from 'react';
import ReactDOM from 'react-dom';
import './css/index.css';
import App from './components/App';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();


class Car extends React.Component {
    render(){
        return <h2> Hi, I am a car </h2>;
    }
}

ReactDOM.render(<Car /> , document.getElementById('car'));
