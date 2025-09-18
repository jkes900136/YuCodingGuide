# Vue 3 Composition API

Composition API算是Vue3帶�??��??�件(component)實�??��?，�?不�?Vue3以�??��??�能使用，�??�以?�Vue2.7以�??��??�直?�撰寫�?

如�?使用Vue2.6(??以�??��??�呢�?

@vue/composition-api就是?��?案�??��?，只要以npm安�?它�??��?維護不�??�難事�?

```powershell
npm install @vue/composition-api
```

?�於一?��??��??�在?��?檔�??�件Single-File Components (SFCs)編寫?�輯程�?碼�?話�??��?將�?輯寫?�\<script setup>?��??�面?�件?��?義在\<template>?��?

如此程�?碼就顯�?簡�?~~?��?~~\~

```html
<script setup>
import { ref, onMounted } from 'vue'
// reactive state
const count = ref(0)

// functions that mutate state and trigger updates
function increment() {
  count.value++
}

// lifecycle hooks
onMounted(() => {
  console.log(`The initial count is ${count.value}.`)
})
</script>
<template>
  <button @click="increment">Count is: {{ count }}</button>
</template>
```

setup實�?上�?不�?形�?，若要跨檔�??�件?�發程�??�話，就?��?將setup以函?��?形�??�獨?�寫??

```html
<script>
import { reactive } from 'vue'

export default {
  setup() {
    const state = reactive({ count: 0 })

    function increment() {
      state.count++
    }

    // don't forget to expose the function as well.
    return {
      state,
      increment
    }
  }
}
</script>
<template>
  <button @click="increment">Count is: {{ count }}</button>
</template>
```

#### props ??emits&#x20;

以props?��?外部?�數，透�?emits?��??�數

```typescript
props:['id'], 
setup(props, context) { 
console.log(props.id) // ?��??�數 
context.emit('done'); // ?��??�數
}
```

#### 好用?�watch

?��??��?件�?變數?��??��?，�??�撰寫�?程�?也能很聰?�\~ &#x20;

```typescript
  watch(id, (newValue, oldValue) => { // ????�數 
  }); 
  watch(()=>obj.id, (newValue, oldValue) => { // ????�件
   });
 watchEffect(() => { // ?��????使用?��?變數 
 fetchData(); // ?��? props?�id ?��??��?就�??��??��? fetchData()
 // ??props?�id ?�在?��??�JavaScript?��?語�??�裡?��??�無作用
  }) 
 
 const fetchData = () => { 
     if (props.id){         
        ...            
      }
  }
```
