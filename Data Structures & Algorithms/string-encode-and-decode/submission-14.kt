class Solution {

    fun encode(strs: List<String>): String {
        val res:String =""

        val strs = strs.map { if (it.isEmpty()) "0#" else "${it.length}#${it}" }
        print("encode--" + strs)
        return strs.joinToString("")
    }

    fun decode(str: String): List<String> {
        val listOfStr: MutableList<String> = mutableListOf()
        var saveBuffer = ""
        var counterValue = ""
        var counter: Int = 0
        for (s in str) {
            
            if (counter != 0) {
                saveBuffer = "${saveBuffer}${s}"
                counter--
                if (counter == 0) {
                    listOfStr.add(saveBuffer)
                    saveBuffer = ""
                }
            } else if (s.isDigit()) {
                counterValue = "${counterValue}${s}"
            } else if (s == '#' && counter == 0) {
                if (counterValue == "0"){
                    listOfStr.add(saveBuffer)
                }
                counter = counterValue.toIntOrNull() ?: 0
                counterValue = ""
            }
        }

        return listOfStr
    }
}
