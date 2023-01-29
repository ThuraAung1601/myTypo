# myTypo
myTypo is a python package to simulate typographical errors in Myanmar language. It was built based on the package "typo" for English Language.

### Usage

```python
import myTypo

myStrError = myTypo.StrError('ကျန်းကျန်းမာမာ ချမ်းချမ်းသာသာ ဘေးရန် ကာစီးသည်', seed=2)
print(myStrError.missing_char().result)
# Should print "ကျ်းကျန်းမာမာ ချမ်းချမ်းသာသာ ဘေးရန် ကာစီးသည်"
print(myStrError.nearby_char().result)
# Should print "ကျ်းကျိ်းမာမာ ချမ်းချမ်းသာသာ ဘေးရန် ကာစီးသည်"

myStrError1 = myTypo.StrError('လူမွဲတွေက မနှေး ခေတ်မီ သူဌေး ဖြစ်တော့မည်', seed=1)
print(myStrError1.nearby_char().result)
# Should print "လူမွဲတွေက ိနှေး ခေတ်မီ သူဌေး ဖြစ်တော့မည်"
print(myStrError1.missing_char().result)
# Should print "လူမွဲတွေက ိှေး ခေတ်မီ သူဌေး ဖြစ်တော့မည်"

```
Currently, following types of typos can be simulated:

Input sentences are
- "ကျန်းကျန်းမာမာ ချမ်းချမ်းသာသာ ဘေးရန် ကာစီးသည်" and
- "လူမွဲတွေက မနှေး ခေတ်မီ သူဌေး ဖြစ်တော့မည်"

**String typos:** 

| Error type    | Description                                                               | Output                             |
|---------------|---------------------------------------------------------------------------|------------------------------------|
| char_swap     | Swaps two random consecutive word characters in the string.               | လူိွဲတွေက နမှေး ခေတ်မီ သူဌေး ဖြစ်တော့မည်       |
| missing_char  | Skips a random word character in the string.                              | ကျ်းကျန်းမာမာ ချမ်းချမ်းသာသာ ဘေးရန် ကာစီးသည်  |
| extra_char    | Adds an extra, keyboard-neighbor, letter next to a random word character. | ကျိန်းကျန်းမာမာ ချမ်းချမ်းသာသာ ဘေးရန် ကာစီးသည်  |
| nearby_char   | Replaces a random word character with keyboard-neighbor letter.           | လူမွဲတွေက မနှေး ခေန်မီ သူဌေး ဖြစ်တော့မည်          |
| random_space  | Adds a random space in the string.                                        |ကျန ်းကျန်းမာမာ ချမ်းချမ်းသာသာ ဘေးရန် ကာစီးသည် |
| repeated_char | Repeats a random word character.                                          |ကျနန်းကျန်းမာမာ ချမ်းချမ်းသာသာ ဘေးရန် ကာစီးသည်  |
