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
Currently, following types of typos can be simulated for text data type:

Given the input sentence "ကျန်းကျန်းမာမာ ချမ်းချမ်းသာသာ ဘေးရန် ကာစီးသည်", different error types produce the following errors.

**String typos:** 

| Error type    | Description                                                               | Output                             |
|---------------|---------------------------------------------------------------------------|------------------------------------|
| char_swap     | Swaps two random consecutive word characters in the string.               | ကျန်းကျန်းမာမာ ချမ်းချမ်းသာသာ ဘေးနရ် ကာစီးသည်       |
| missing_char  | Skips a random word character in the string.                              | ကျ်းကျန်းမာမာ ချမ်းချမ်းသာသာ ဘေးရန် ကာစီးသည်  |
| extra_char    | Adds an extra, keyboard-neighbor, letter next to a random word character. | ကျိန်းကျန်းမာမာ ချမ်းချမ်းသာသာ ဘေးရန် ကာစီးသည်  |
| nearby_char   | Replaces a random word character with keyboard-neighbor letter.           | ကျိ်းကျန်းမာမာ ချမ်းချမ်းသာသာ ဘေးရန် ကာစီးသည် |
| random_space  | Adds a random space in the string.                                        |ကျန ်းကျန်းမာမာ ချမ်းချမ်းသာသာ ဘေးရန် ကာစီးသည် |
| repeated_char | Repeats a random word character.                                          |ကျနန်းကျန်းမာမာ ချမ်းချမ်းသာသာ ဘေးရန် ကာစီးသည်  |



### Reference
- Ranvijay Kumar, typo: "About A python package to simulate typographical errors". Github Link: https://github.com/ranvijaykumar/typo

### Todo
- Update the simulator to simulate spelling errors by using edit distance approach
- Update the simulator for common spelling errors in both syllable and word levels
