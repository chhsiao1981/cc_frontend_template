import React, { PureComponent } from 'react'
import Immutable from 'immutable'
import { getUUID, getRootId, getRoot, getChildId, getChildIds } from '../utils/utils'
import Empty from '../components/Empty'

import styles from './Simple.module.css'

class Simple extends PureComponent {
  render() {
    const {myId, simple, actions: {doSimple}} = this.props
    if(!myId) return (<Empty />)

    let me = simple.get(myId, Immutable.Map())

    const onClickRemove = (e) => {
      doSimple.remove(myId)
    }

    return (
        <div>Hello Simple: {myId}
          <button onClick={onClickRemove}>Remove</button>
        </div>
    )
  }
}

export default Simple
