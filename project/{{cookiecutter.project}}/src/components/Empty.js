import React, { PureComponent } from 'react'
import styles from './Empty.module.css'

class Empty extends PureComponent {
  render() {
    return <div className={styles['hide']}></div>
  }
}

export default Empty
