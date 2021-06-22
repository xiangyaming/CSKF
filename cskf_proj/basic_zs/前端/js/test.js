// alert('hello python');

// 变量：需要申明
var name = '小明';
var age;

// 输出到控制台
console.log(name);

// 数据类型：数字 字符串 数组 null undefined Boolean

// 数组：相当于Python的列表
var aList = Array(1, 2, 3, 4, 'a');
aList.push('python');   //数组最后面添加一个元素
aList.pop();            //获取数组的最后一个元素

// undefined 已申明，为赋值
// boolean true false
// ==判断内容是否相等   ===判断内容是否相等且类型相同

var a=18;
var b=10;

if(a>10){
    console.log('你是一个大孩子')
}else {
    console.log('还是一个小孩子')
}

switch (a-b) {
    case 5:
        console.log(5);
        break;
    case 8:
        console.log(8);
        break;
    default:
        console.log('以上结果都不对')
}

function add(a,b) {
    return a+b
}
add(10,20);

// 对象 obj.name obj['name']调用
var obj={
    name : '小明',
    fun :function add(a,b) {
    return a+b
    }
};