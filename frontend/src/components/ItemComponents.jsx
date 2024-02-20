import { useQuery } from "react-query";
import "./ItemComponents.css"
import { useState } from "react";

export function Item({item,  onClick, className}) {
    let defaultClick = () => {console.log(`${item.name} was clicked with no op`)}
    onClick = onClick ?? defaultClick
    className = className ?? ""

    // EmptyItem
    if(!item) {
        return (
            <div className={"item " + className} onClick={defaultClick}>
            </div>
        )
    }

    // Item
    const IMG_ADDRESS = `http://127.0.0.1:8090/api/files/item/${item.id}/${item.image}`
    return(
        <div className={"item " + className} onClick={defaultClick}>
            <img src={IMG_ADDRESS} alt={item.name} draggable="false"/>
            <div>{item?.name}</div>
        </div>
    )
}

export function ItemList({items}) {
    const [selected, setSelected] = useState()
    console.log(`selected is ${selected}`)
    const toggle = (i) => {
        {
            if(selected === i.id) {
                setSelected(undefined)
            } else {
                setSelected(i.id)
            }
        }
    }

    return(
        <div className="item-list">
            {items.map((item) => (
                <Item key={item.id} item={item} onClick={() => toggle(item)} 
                className={selected === item.id ? 'item-highlighted' : ''} />
            ))}
        </div>
    )
}

export function ItemListQuery() {
    const ITEMS_ADDRESS = "http://127.0.0.1:8090/api/collections/item/records"
    const { data } = useQuery({
        queryKey: ["items"],
        queryFn: () => (
          fetch(ITEMS_ADDRESS) // item records
            .then((response) => response.json())
        ),
      });
    if(data?.items) {
        return (
            <ItemList items={data.items}/>
        )
    }
    return (
        <div>
            No Items available: Trouble loading {ITEMS_ADDRESS}
        </div>
    )

}

export function ItemGrid({items, row, col}) {
    const DEFAULT_ROW = 3
    const DEFUALT_COL = 4
    row = row ?? DEFAULT_ROW
    col = col ?? DEFUALT_COL
    if(!items) {
        return (
            <div style={{color:'red'}}>
                ERROR LOADING GRID ITEMS: {items}
            </div>
        )
    }
    
    if (items.length > row * col) {
        throw new Error("Number of items exceeds the grid capacity");
    }
    let grid_style = {
        gridTemplateRows: `repeat(${row}, 1fr)`,
        gridTemplateColumns: `repeat(${col}, 1fr)`
    }

    const renderedItems = [];
    for (let i = 0; i < row*col; i++) {
        const item = items[i];
        renderedItems.push(<Item key={item?.id ?? `empty-config-grid-item-${i}`} item={item} />);
    }
      
    return (
    <div className="item-grid" style={grid_style}>
        {renderedItems}
    </div>
    )
}