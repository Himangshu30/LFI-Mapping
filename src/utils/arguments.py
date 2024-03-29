import argparse
from src.utils.banner import BannerHelpFormatter

print("")
parser = argparse.ArgumentParser(description='LFImap, Local File Inclusion discovery and exploitation tool', formatter_class=BannerHelpFormatter, add_help=False)

mandatoryGroup = parser.add_argument_group("TARGET OPTIONS")
mandatoryGroup.add_argument('-U', type=str,nargs='?', metavar='url', dest='url', help='\t\t Specify single url to test')
mandatoryGroup.add_argument('-F', type=str, nargs='?', metavar='urlfile', dest='f', help='\t\t Specify multiple urls to test from a file')
mandatoryGroup.add_argument('-R', type=str, nargs='?', metavar='reqfile', dest='reqfile', help='\t\t Specify single raw request to test from a file')

optionsGroup = parser.add_argument_group('GENERAL OPTIONS')
optionsGroup.add_argument('-C', type=str, metavar='<cookie>', dest='cookie', help='\t\t Specify session Cookie header')
optionsGroup.add_argument('-D', type=str, metavar='<data>', dest='postreq', help='\t\t Specify request FORM-data')
#optionsGroup.add_argument('-J', type=str, metavar='<json>', dest='json', help='\t\t Specify request JSON FORM-data')
optionsGroup.add_argument('-H', type=str, metavar='<header>', action='append', dest='httpheaders', help='\t\t Specify additional HTTP header(s)')
optionsGroup.add_argument('-M', type=str, metavar='<method>', dest='method', help='\t\t Specify request method to use for testing')
optionsGroup.add_argument('-P', type=str, metavar = '<proxy>', dest='proxyAddr', help='\t\t Specify proxy URL:PORT')
optionsGroup.add_argument('--useragent', type=str, metavar= '<agent>', dest='agent', help='\t\t Specify HTTP user-agent header value')
optionsGroup.add_argument('--referer', type=str, metavar = '<referer>', dest='referer', help='\t\t Specify HTTP referer header value')
optionsGroup.add_argument('--placeholder', type=str, metavar='<name>', dest='param', help='\t\t Specify custom testing placeholder name (default is "PWN")')
optionsGroup.add_argument('--delay', type=int, metavar='<milis>', dest='delay', help='\t\t Specify delay in miliseconds after each request')
optionsGroup.add_argument('--max-timeout', type=int, metavar='<seconds>', dest='maxTimeout', help='\t\t Specify number of seconds after giving up on a URL (default 5)')
optionsGroup.add_argument('--http-ok', type=int, action='append', metavar='<number>', dest='http_valid', help='\t\t Specify http response code(s) to treat as valid')
optionsGroup.add_argument('--force-ssl', action='store_true', dest = 'force_ssl', help='\t\t Force usage of HTTPS/SSL if otherwise not specified')
optionsGroup.add_argument('--no-stop', action='store_true', dest = 'no_stop', help='\t\t Don\'t stop using the same testing technique upon findings')

attackGroup = parser.add_argument_group('ATTACK TECHNIQUE')
attackGroup.add_argument('-f', '--filter', action = 'store_true', dest = 'php_filter', help='\t\t Attack using filter wrapper')
attackGroup.add_argument('-i', '--input', action = 'store_true', dest = 'php_input', help='\t\t Attack using input wrapper')
attackGroup.add_argument('-d', '--data', action = 'store_true', dest = 'php_data', help='\t\t Attack using data wrapper')
attackGroup.add_argument('-e', '--expect', action = 'store_true', dest = 'php_expect', help='\t\t Attack using expect wrapper')
attackGroup.add_argument('-t', '--trunc', action = 'store_true', dest = 'trunc', help='\t\t Attack using path traversal with wordlist (default "short.txt")')
attackGroup.add_argument('-r', '--rfi', action = 'store_true', dest = 'rfi', help='\t\t Attack using remote file inclusion')
attackGroup.add_argument('-c', '--cmd', action = 'store_true', dest = 'cmd', help='\t\t Attack using command injection')
attackGroup.add_argument('-file', '--file', action = 'store_true', dest='file', help='\t\t Attack using file wrapper')
attackGroup.add_argument('-heur', '--heuristics', action= 'store_true', dest= 'heuristics', help= '\t\t Test for miscellaneous issues using heuristics')
attackGroup.add_argument('-a', '--all', action = 'store_true', dest = 'test_all', help='\t\t Use all supported attack methods')

#enumGroup = parser.add_argument_group('ENUMERATION OPTIONS')
#enumGroup.add_argument('-eS', '--enum-system', action = 'store_true', dest='enum_system', help='\t\t Specify to enumerate operating system')
#enumGroup.add_argument('-eF', '--enum-files', action = 'store_true', dest='enum_files', help='\t\t Specify to enumerate file system')
#enumGroup.add_argument('-eU', '--enum-users', action = 'store_true', dest='enum_users', help='\t\t Specify to enumerate existing users')
#enumGroup.add_argument('-eP', '--enum-proc', action = 'store_true', dest='enum_proc', help='\t\t Specify to enumerate processes and programs')
#enumGroup.add_argument('-eN', '--enum-net', action = 'store_true', dest='enum_net', help='\t\t Specify to enumerate network configuration')
#enumGroup.add_argument('-eA', '--enum-all', action= 'store_true', dest='enum_all', help='\t\t Specify to utilize all enumeration options')

payloadGroup = parser.add_argument_group('PAYLOAD OPTIONS')
payloadGroup.add_argument('-n', type=str, action='append', metavar='<U|B>', dest='encodings', help='\t\t Specify payload encoding(s). "U" for URL, "B" for base64')
payloadGroup.add_argument('-q','--quick', action='store_true', dest='quick', help='\t\t Perform quick testing with fewer payloads')
payloadGroup.add_argument('-x', '--exploit',action='store_true', dest='revshell', help='\t\t Exploit and send reverse shell if RCE is available')
payloadGroup.add_argument('--lhost', type=str, metavar='<lhost>', dest='lhost', help='\t\t Specify local ip address for reverse connection')
payloadGroup.add_argument('--lport', type=int, metavar='<lport>', dest='lport', help='\t\t Specify local port number for reverse connection')
payloadGroup.add_argument('--callback', type=str, metavar='<hostname>', dest='callback', help='\t\t Specify callback location for rfi and cmd detection')
#payloadGroup.add_argument('--check-url', type=str, metavar='<path>', dest='getvuln', help='\t\t Specify url to check if stored payload triggered successfully')
#payloadGroup.add_argument('--read-file', type=str, metavar='<file>', dest='readfile', help='\t\t Specify file path to leak if LFR is available')
#payloadGroup.add_argument('--execute-cmd', type=str, metavar='<command>', dest='command', help='\t\t Specify command to execute if RCE is available')

wordlistGroup = parser.add_argument_group('WORDLIST OPTIONS')
wordlistGroup.add_argument('-wT', type=str, metavar = '<path>', dest='truncWordlist', help='\t\t Specify path to wordlist for path traversal modality')
wordlistGroup.add_argument('--use-long', action='store_true', dest='uselong', help='\t\t Use "src/wordlists/long.txt" wordlist for path traversal modality')

outputOptions = parser.add_argument_group('OUTPUT OPTIONS')
#outputOptions.add_argument('-oH', type=str, metavar='<htmlfile>', dest='htmlfile', help='\t\t Output findings to html file')
#outputOptions.add_argument('-oT', type=str, metavar='<txtfile>', dest='txtfile', help='\t\t Output findings to txt file')
#outputOptions.add_argument('-oX', type=str, metavar='<xmlfile>', dest='xmlfile', help='\t\t Output findings to xml file')
#outputOptions.add_argument('-oA', type=str, metavar='<allfile>', dest='allfile', help='\t\t Output to all supported formats')
outputOptions.add_argument('--log', type=str, metavar='<logfile>', dest='log', help='\t\t Output all requests and responses to specified file')

otherGroup = parser.add_argument_group('OTHER')
otherGroup.add_argument('-v', '--verbose', action='store_true', dest='verbose', help='\t\t Print more detailed output when performing attacks\n')
otherGroup.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='\t\t Print this help message\n\n')

args = parser.parse_args()
