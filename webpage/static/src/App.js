import React, { Component } from 'react';
import { ImageLoader } from './ImageLoader';
import { Visor } from './Visor';

import './App.css';


class App extends Component {
  
  render() {return (
      <React.Fragment>
  
        <ImageLoader></ImageLoader>
        {/* <Visor image={image}></Visor> */}
        
      </React.Fragment>
    );
  }
}
  
export default App;