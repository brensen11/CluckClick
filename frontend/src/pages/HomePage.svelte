<script lang="ts">
    import ItemGrid from '../lib/ItemGrid.svelte'
    import type {ItemData} from '../api/entities.ts';

    let items: Array<ItemData> = [
        {name:'hello', image:'beans'},
        {name:'hello', image:'beans'},
        {name:'hello', image:'beans'},
        {name:'hello', image:'beans'},
        {name:'hello', image:'beans'},
        {name:'hello', image:'beans'}
    ]

//   do some queries for items and columns
</script>

<div>
  <ItemGrid data={items} columns={3}></ItemGrid>
</div>
