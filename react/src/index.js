import React, { PureComponent} from 'react';
import ReactDOM from 'react-dom';
import './css/index.css';
import DocumentList from './components/App';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<DocumentList />, document.getElementById('root'));
registerServiceWorker();



//const styles = {
//    li:{
//        display:"flex",
//        justifyContent:"flex-start".
//        background:"white",
//        boxShadow:"2px 4px 10px rgba(0,0,0,0.2)",
//        color:"#707070",
//        marginBottom:"1em",
//        cursor:"pointer"
//    },
//    leftWall: color => ({
//        width:"0.5em",
//        backgroundColor: color
//    })
//};
//
//export default class ListItem extends PureComponent{
//    render(){
//        return (
//            <li style={styles.li}>
//                <div style={styles.leftWall(this.prop)}
//            </li>
//
//
//        )
//    }
//}

//class Car extends React.Component {
//    render(){
//        return <h2> Hi, I am a car </h2>;
//    }
//}

//class FilesList extends Component{
//    constructor(props){
//        super(props)
//        this.state = {
//        documents:{
//          id:1,
//          name: "Gently on my mind",
//          description: "Molly Tuttle"
//        }
//      }
//    }
//    render(){
//        const { documents } = this.state
//        return (<div className="App"><h1> FilesList </h1> </div>);
//    }
//}
//
//ReactDOM.render(<Car /> , document.getElementById('car'));
//ReactDOM.render(<FilesList />,
//  document.getElementById('files_list')
//);
