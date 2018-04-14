from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1211   ._SN',
        MapName             = 'Bose',
        Location            = 'T1210.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '阿加特',                               # 9
        '提妲',                                 # 10
        '阿加特',                               # 11
        '锅',                                   # 12
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH00050 ._CH',             # 00
        'ED6_DT07/CH00060 ._CH',             # 01
        'ED6_DT26/CH20365 ._CH',             # 02
        'ED6_DT26/CH20351 ._CH',             # 03
        'ED6_DT26/CH20350 ._CH',             # 04
        'ED6_DT26/CH20366 ._CH',             # 05
        'ED6_DT26/CH20206 ._CH',             # 06
        'ED6_DT26/CH20205 ._CH',             # 07
        'ED6_DT26/CH20425 ._CH',             # 08
        'ED6_DT26/CH20455 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH00050P._CP',             # 00
        'ED6_DT07/CH00060P._CP',             # 01
        'ED6_DT26/CH20365P._CP',             # 02
        'ED6_DT26/CH20351P._CP',             # 03
        'ED6_DT26/CH20350P._CP',             # 04
        'ED6_DT26/CH20366P._CP',             # 05
        'ED6_DT26/CH20206P._CP',             # 06
        'ED6_DT26/CH20205P._CP',             # 07
        'ED6_DT26/CH20425P._CP',             # 08
        'ED6_DT26/CH20455P._CP',             # 09
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_17A",          # 00, 0
        "Function_1_1B6",          # 01, 1
        "Function_2_1BE",          # 02, 2
        "Function_3_1742",         # 03, 3
        "Function_4_2AB7",         # 04, 4
    )


    def Function_0_17A(): pass

    label("Function_0_17A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_199")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x53), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 2)
    Jump("loc_1B5")

    label("loc_199")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_1B5")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_1B5")

    Return()

    # Function_0_17A end

    def Function_1_1B6(): pass

    label("Function_1_1B6")

    OP_B1("T1211")
    Return()

    # Function_1_1B6 end

    def Function_2_1BE(): pass

    label("Function_2_1BE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    OP_6D(-25200, 0, 47910, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x8, -24200, 400, 47000, 0)
    SetChrPos(0x9, -28470, 0, 41130, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 7)
    SetChrSubChip(0x9, 0)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 2)
    SetChrSubChip(0x8, 0)
    SetChrFlags(0x8, 0x4)
    OP_6F(0x0, 10)
    SetChrPos(0xB, -29470, 700, 41170, 0)
    ClearChrFlags(0xB, 0x80)
    LoadEffect(0x0, "map\\\\onsen00.eff")
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS106._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS192._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS193._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS194._CH")
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("少女的声音")

    AnonymousTalk(    #0
        (
            "\x07\x0C……我说，哥哥…………\x02\x03",

            "…………哥哥啊…………………\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 1500, 0)
    Sleep(2000)
    SetMessageWindowPos(320, 260, -1, -1)
    SetChrName("红发少女")

    AnonymousTalk(    #1
        (
            "\x07\x0C嘿嘿，这次的生日，\x01",
            "你可要期待着哦。\x02\x03",

            "我会送给哥哥你\x01",
            "看了就会很高兴的礼物⊙\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("红发少年")

    AnonymousTalk(    #2
        (
            "\x07\x0C是吗……\x01",
            "我看了会高兴的东西啊。\x02\x03",

            "你是不是要做什么\x01",
            "好吃的给我？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(320, 260, -1, -1)
    SetChrName("红发少女")

    AnonymousTalk(    #3
        (
            "\x07\x0C真是的～怎么想到吃上面去了。\x02\x03",

            "生日礼物当然应该是\x01",
            "可以保存的有形的东西啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("红发少年")

    AnonymousTalk(    #4
        (
            "\x07\x0C那种东西吗？\x02\x03",

            "嗯～有形的，\x01",
            "我看了又会高兴的东西……\x02\x03",

            "是能用来打猎的小刀？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(320, 260, -1, -1)
    SetChrName("红发少女")

    AnonymousTalk(    #5
        (
            "\x07\x0C你不是刚从村长\x01",
            "那里拿到了小刀嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(320, 260, -1, -1)
    SetChrName("红发少女")

    AnonymousTalk(    #6
        (
            "\x07\x0C答案是我亲手做的\x01",
            "首饰！\x02\x03",

            "虽然还没完成。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("红发少年")

    AnonymousTalk(    #7
        (
            "\x07\x0C你、你等等！\x02\x03",

            "我又不是女人，\x01",
            "要首饰干吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(320, 260, -1, -1)
    SetChrName("红发少女")

    AnonymousTalk(    #8
        (
            "\x07\x0C哥哥已经～\x01",
            "和时代脱节了啦。\x02\x03",

            "男孩子只要戴上一件\x01",
            "装饰的首饰\x01",
            "就会变得很酷的哦。\x02\x03",

            "一定能让外表冷冰冰的\x01",
            "哥哥变得有人气的哦⊙\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("红发少年")

    AnonymousTalk(    #9
        "\x07\x0C我说啊……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(320, 260, -1, -1)
    SetChrName("红发少女")

    AnonymousTalk(    #10
        (
            "\x07\x0C不可以……吗？\x02\x03",

            "我想对平时照顾\x01",
            "我的哥哥表示感谢……\x02\x03",

            "拼命在做着……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("红发少年")

    AnonymousTalk(    #11
        (
            "\x07\x0C唔……\x02\x03",

            "不、不是那种很可爱，很\x01",
            "艳丽的吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(320, 260, -1, -1)
    SetChrName("红发少女")

    AnonymousTalk(    #12
        (
            "\x07\x0C嘿嘿，不用担心。\x02\x03",

            "简单又帅气的造型，\x01",
            "十分适合哥哥的。\x02\x03",

            "哥哥个子又高，\x01",
            "肯定很合适的。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("红发少年")

    AnonymousTalk(    #13
        (
            "\x07\x0C好～知道了知道了。\x02\x03",

            "我会尽量期待的，\x01",
            "加油做吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(320, 260, -1, -1)
    SetChrName("红发少女")

    AnonymousTalk(    #14
        (
            "\x07\x0C嘿嘿……嗯！\x02\x03",

            "我说，哥哥。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(    #15
        "\x07\x0C怎么了，米夏？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x3, 0x4, 0, 0, 0)
    OP_C6(0x3, 0x3, 16777215, 0, 0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(320, 260, -1, -1)
    SetChrName("米夏")

    AnonymousTalk(    #16
        (
            "\x07\x0C一直以来，谢谢你。\x02\x03",

            "总是保护着我……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    OP_C6(0x3, 0x3, 16777215, 1000, 0)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    Sleep(3000)
    PlayEffect(0x0, 0x0, 0xB, 300, 400, -300, 0, 0, 0, 300, 200, 300, 0xFF, 0, 0, 0, 0)
    FadeToBright(2000, 16777215)
    OP_0D()
    Sleep(500)
    OP_99(0x8, 0xA, 0xB, 0x3E8)
    Sleep(500)

    ChrTalk(    #17
        0x8,
        "#1281F#5P啊……\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x258, 1400, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x8)
    OP_99(0x8, 0xB, 0xA, 0x3E8)
    Sleep(100)
    SetChrSubChip(0x8, 0)
    Sleep(500)

    ChrTalk(    #18
        0x8,
        "#1282F#5P是……梦啊。\x02",
    )

    CloseMessageWindow()
    OP_99(0x8, 0xA, 0xB, 0x3E8)
    Sleep(100)
    SetChrSubChip(0x8, 15)
    Sleep(500)

    ChrTalk(    #19
        0x8,
        "#1289F#5P这里是……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #20
        0x9,
        "少女的声音",
        "#2P……嗯，这样就行了吧。\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x258, 1400, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x8, 11)
    Sleep(100)
    SetChrSubChip(0x8, 12)

    ChrTalk(    #21
        0x8,
        "#1281F#2P米夏……？\x02",
    )

    CloseMessageWindow()
    OP_6D(-27180, 0, 44810, 2000)
    OP_62(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #22
        0x9,
        (
            "#1264F#5P阿加特哥哥！？\x02\x03",

            "#1261F太好了……\x01",
            "你醒了啊！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BEB():
        OP_8E(0xFE, 0xFFFF9C78, 0x0, 0xB644, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_BEB)

    def lambda_C06():
        OP_6D(-25360, 0, 48370, 2000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_C06)
    WaitChrThread(0x9, 0x1)
    OP_8C(0x9, 90, 400)
    WaitChrThread(0x9, 0x2)

    ChrTalk(    #23
        0x8,
        "#1281F#4P小鬼头……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x9,
        (
            "#1263F#5P那个那个，你身体\x01",
            "不要紧了吗……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        "#1280F#4P嗯，没什么──\x02",
    )

    CloseMessageWindow()
    OP_B0(0x0, 0xA)
    OP_6F(0x0, 10)
    OP_70(0x0, 0x28)
    OP_99(0x8, 0x0, 0x4, 0x384)
    OP_9E(0x8, 0x14, 0x0, 0x12C, 0xBB8)
    Sleep(500)

    ChrTalk(    #26
        0x8,
        "#1285F#4P痛……\x02",
    )

    OP_99(0x8, 0x7, 0x9, 0x4B0)
    CloseMessageWindow()
    OP_62(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #27
        0x9,
        (
            "#1265F#5P不、不行的～！\x01",
            "你必须老老实实地躺着！\x02\x03",

            "伤口还没有\x01",
            "完全愈合！\x02",
        )
    )

    CloseMessageWindow()
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 40)
    OP_70(0x0, 0x3C)
    OP_99(0x8, 0x9, 0x7, 0x3E8)
    OP_99(0x8, 0x4, 0x6, 0x3E8)
    Sleep(500)

    ChrTalk(    #28
        0x8,
        (
            "#1280F#4P去，这点伤算不了\x01",
            "什么的。\x02\x03",

            "不管它自己也会好起来的……\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 9)
    SetChrSubChip(0x9, 0)
    OP_99(0x9, 0x0, 0x1, 0x7D0)
    Sleep(250)

    ChrTalk(    #29
        0x9,
        "#1268F#5P#3S不、不行！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    SetChrSubChip(0x9, 5)
    OP_0D()
    Sleep(250)
    OP_99(0x9, 0x5, 0x3, 0x5DC)
    Sleep(500)

    ChrTalk(    #30
        0x9,
        (
            "#1262F#5P我和姐姐\x01",
            "说好了！\x02\x03",

            "在阿加特哥哥恢复之前\x01",
            "绝对不让你下床！\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x8, 0x12, 0x14, 0x4B0)
    Sleep(250)

    ChrTalk(    #31
        0x8,
        "#1281F#4P喂、喂……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x9,
        "#1262F#5P唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        "#1284F#4P明白了，明白了啦。\x02",
    )

    CloseMessageWindow()
    OP_99(0x8, 0x14, 0x12, 0x3E8)
    Sleep(100)
    OP_6F(0x0, 30)
    OP_70(0x0, 0xA)
    OP_99(0x8, 0x6, 0x0, 0x3E8)
    Sleep(800)

    ChrTalk(    #34
        0x9,
        "#1271F#5P……呼…………\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 7)
    SetChrSubChip(0x9, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #35
        0x8,
        (
            "#1282F#4P真是的……\x01",
            "那么激动。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x8, 0xA, 0xB, 0x4B0)
    OP_99(0x8, 0xB, 0xC, 0x4B0)
    Sleep(300)

    ChrTalk(    #36
        0x8,
        (
            "#1281F#4P说起来，已经是晚上了啊。\x02\x03",

            "艾丝蒂尔她们怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x9,
        (
            "#1260F#5P嗯，姐姐她们已经\x01",
            "先回柏斯去了。\x02\x03",

            "好像她们有和将军的约定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        "#1284F#4P和将军的约定？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #39
        "\x07\x05提妲向阿加特传达了艾丝蒂尔的口信。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #40
        0x8,
        (
            "#1280F#4P……是吗，\x01",
            "说动了那个摩尔根啊。\x02\x03",

            "那么，军队也该\x01",
            "联络协会了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 11)
    Sleep(500)

    ChrTalk(    #41
        0x8,
        "#1283F#4P好，那么我也快点……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x9,
        "#1262F#5P…………………（盯。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x8,
        (
            "#1288F#4P……不过\x01",
            "今天已经太晚了。\x02\x03",

            "#1280F明早再回\x01",
            "柏斯吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x9,
        "#1265F#5P可、可是……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 12)
    Sleep(300)

    ChrTalk(    #45
        0x8,
        (
            "#1280F#4P睡得很充足，\x01",
            "体力也恢复了很多。\x02\x03",

            "而且都是一些擦伤，\x01",
            "这伤就算活动着也会自然好的。\x02\x03",

            "没问题，不用担心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x9,
        "#1263F#5P你没……硬撑吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "#1293F#4P我说啊，我可是一名正游击士。\x02\x03",

            "我还没有莽撞到面对结社和龙\x01",
            "都敢硬撑的程度啊。\x02\x03",

            "#1289F……而且也不能再让你\x01",
            "继续遇险了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        "#1264F#5P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        (
            "#1280F#4P反正我可没胆量\x01",
            "得罪可怕的督察员小姐。\x02\x03",

            "就彻底相信我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x9,
        (
            "#1271F#5P真、真是的……\x01",
            "阿加特哥哥你这人……\x02\x03",

            "#1260F不过看起来\x01",
            "真的挺精神的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        (
            "#1280F#4P所以我就说嘛。\x02\x03",

            "自己的身体自己\x01",
            "最清楚了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x9,
        (
            "#1266F#5P嘿嘿……太好了。\x02\x03",

            "#1269F…………啊………………\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 4)
    SetChrSubChip(0x9, 0)
    OP_99(0x9, 0x0, 0x6, 0x3E8)
    OP_62(0x8, 0x258, 1400, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #53
        0x8,
        "#1284F#4P怎、怎么了！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        "#1272F#5P呜……呜……\x02",
    )

    CloseMessageWindow()
    OP_B0(0x0, 0xA)
    OP_6F(0x0, 10)
    OP_70(0x0, 0x3C)
    OP_99(0x8, 0x0, 0x6, 0x5DC)
    OP_99(0x8, 0x12, 0x14, 0x5DC)
    OP_62(0x8, 0x0, 1600, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #55
        0x8,
        (
            "#1284F#4P我、我都说了我\x01",
            "已经没事了啦！\x02\x03",

            "我对女神发誓\x01",
            "我没撒谎！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        (
            "#1272F#5P呜……\x01",
            "……不、不是的……\x02\x03",

            "一放下心来……我就……\x01",
            "不知道怎么的………\x02\x03",

            "#1269F呜呜呜……\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x9, 0x7, 0xB, 0x3E8)
    Sleep(300)

    ChrTalk(    #57
        0x9,
        "#1268F#5P#4S呜哇啊啊啊啊啊啊……！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)

    def lambda_1539():

        label("loc_1539")

        OP_99(0xFE, 0xB, 0xD, 0x3E8)
        OP_48()
        Jump("loc_1539")

    QueueWorkItem2(0x9, 1, lambda_1539)
    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        (
            "#1288F#4P啊～……\x02\x03",

            "#1290F真拿你没办法。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(800)
    SetChrPos(0x8, -25540, 0, 46100, 270)
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x8, 0)
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 20)
    OP_70(0x0, 0xA)
    OP_6D(-26020, 0, 47720, 1000)
    OP_0D()
    OP_8C(0x8, 0, 400)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x2)
    OP_44(0x9, 0x1)
    SetChrSubChip(0x9, 16)
    Sleep(1000)
    OP_99(0x9, 0x11, 0x16, 0x3E8)

    def lambda_15F0():

        label("loc_15F0")

        OP_99(0xFE, 0x16, 0x12, 0x3E8)
        OP_48()
        Jump("loc_15F0")

    QueueWorkItem2(0x9, 1, lambda_15F0)
    Sleep(500)

    ChrTalk(    #59
        0x8,
        (
            "#1290F#6P……对不起。\x01",
            "让你那么担心。\x02\x03",

            "一个人昏了头的冲出去，\x01",
            "还打了一场没有胜算的架……\x02\x03",

            "想不到最后\x01",
            "还让你那么担心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        (
            "#1269F#2P……就是啊！\x01",
            "阿加特哥哥是个傻瓜！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x9, 0x1)
    OP_99(0x9, 0x17, 0x1F, 0x5DC)
    Sleep(300)

    ChrTalk(    #61
        0x9,
        (
            "#1272F#2P我……我……\x01",
            "我真的很担心的啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x8,
        (
            "#1290F#6P嗯，是啊……\x02\x03",

            "#1291F我真是……一个大傻瓜。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearMapFlags(0x2000000)
    OP_A2(0x10F6)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1BE end

    def Function_3_1742(): pass

    label("Function_3_1742")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    OP_6D(-26550, 0, 42500, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x8, -25540, 0, 46100, 0)
    SetChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x8, 0)
    SetChrPos(0xB, -29470, 700, 41170, 0)
    ClearChrFlags(0xB, 0x80)
    LoadEffect(0x0, "map\\\\onsen00.eff")
    PlayEffect(0x0, 0x0, 0xB, 300, 400, -300, 0, 0, 0, 300, 200, 300, 0xFF, 0, 0, 0, 2000)
    SetChrPos(0x9, -25480, 0, 46660, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 4)
    SetChrSubChip(0x9, 31)
    OP_6F(0x0, 5)

    def lambda_1845():
        OP_6D(-26020, 0, 47720, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1845)

    def lambda_185D():
        OP_67(0, 6150, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_185D)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #63
        0x9,
        "#1271F#2P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x8,
        "#1290F#6P……好一点了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        "#1271F#2P…………（擤鼻子）\x02",
    )

    CloseMessageWindow()
    OP_99(0x9, 0x1F, 0x23, 0x320)
    Sleep(500)

    ChrTalk(    #66
        0x9,
        (
            "#1263F#2P对、对不起。\x01",
            "突然就哭了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        (
            "#1288F#6P真是的，你可别\x01",
            "吓我啊。\x02\x03",

            "真是的，比对付银发小子\x01",
            "还要让人提心吊胆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        (
            "#1267F#2P嘿嘿……\x02\x03",

            "#1264F啊，对了……\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x9, 0x23, 0x21, 0x320)
    Sleep(300)

    ChrTalk(    #69
        0x9,
        (
            "#1260F#2P那个那个，阿加特哥哥。\x01",
            "肚子饿了吗？\x02\x03",

            "我从村长那儿拿了材料\x01",
            "做了热汤……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x8,
        (
            "#1280F#6P喔，怪不得\x01",
            "有一股香味呢。\x02\x03",

            "#1281F……咦，等等。\x02\x03",

            "怎么会有厨房……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x9,
        "#1264F#2P啊……？\x02",
    )

    CloseMessageWindow()
    Fade(500)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 7)
    SetChrSubChip(0x9, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x8, 0)
    OP_0D()

    def lambda_1A8E():
        OP_6D(-27810, 0, 45350, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A8E)
    OP_8C(0x8, 270, 400)
    OP_8C(0x8, 180, 400)
    Sleep(1000)
    OP_8E(0x8, 0xFFFF9AB6, 0x0, 0xAD8E, 0x3E8, 0x0)
    Sleep(500)
    OP_8C(0x8, 90, 400)
    Sleep(500)
    OP_8C(0x8, 270, 400)
    Sleep(1000)

    ChrTalk(    #72
        0x8,
        (
            "#1284F#6P仔细看看……还真让人吃惊。\x02\x03",

            "虽然有点些微的差别，\x01",
            "不过几乎和那时候一模一样啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B46():

        label("loc_1B46")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_1B46")

    QueueWorkItem2(0x9, 1, lambda_1B46)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1B73():
        OP_6D(-26430, 0, 47750, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1B73)
    OP_8C(0x8, 0, 400)
    Sleep(1000)
    OP_8E(0x8, 0xFFFF993A, 0x0, 0xB75C, 0x3E8, 0x0)
    WaitChrThread(0x0, 0x1)
    Sleep(500)

    ChrTalk(    #73
        0x8,
        (
            "#1290F#3P再加上还有这个……\x02\x03",

            "#1291F呵……\x01",
            "想不到这东西还会留存下来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x9,
        "#1264F#4P？？？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)
    Sleep(500)

    ChrTalk(    #75
        0x8,
        (
            "#1290F#5P噢，你不明白是吧。\x02\x03",

            "……其实这个家，\x01",
            "在十年前被完全烧毁了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x9,
        "#1270F#4P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        (
            "#1282F#5P帝国军的燃烧弹\x01",
            "变成流弹射进村里……\x02\x03",

            "一转眼这个屋子都着了火，\x01",
            "瞬间烧成黑炭了。\x02\x03",

            "#1289F我知道后来村长\x01",
            "又好心地重建了起来……\x02\x03",

            "不过没想到连\x01",
            "屋内的布置都和过去一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x9,
        "#1265F#4P…………………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    Sleep(500)

    ChrTalk(    #79
        0x8,
        (
            "#1280F#5P虽然我从来没\x01",
            "进过这里……\x02\x03",

            "不过他们竟能做到这个地步，\x01",
            "还真得去道个谢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x9,
        (
            "#1265F#4P………………………………\x02\x03",

            "……那……那么……\x02\x03",

            "那时……米夏姐姐……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x8,
        (
            "#1282F#5P………………………………\x02\x03",

            "#1290F……哈哈，被你看穿了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 300)

    def lambda_1E59():
        OP_6D(-26720, 0, 47740, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1E59)
    OP_8F(0x8, 0xFFFF97E6, 0x0, 0xB6A8, 0x1F4, 0x0)
    OP_44(0x9, 0x1)
    Fade(1000)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 0)
    SetChrPos(0x8, -26500, 0, 46620, 90)
    OP_0D()
    Sleep(500)
    OP_99(0x8, 0x0, 0x2, 0x320)
    Sleep(500)

    ChrTalk(    #82
        0x8,
        (
            "#1282F#5P……她为我准备了\x01",
            "生日礼物。\x02\x03",

            "亲手做的……\x01",
            "一件十分适合我的首饰。\x02\x03",

            "在去山道避难的途中，那家伙\x01",
            "回家去取那个……\x02\x03",

            "然后燃烧弹就掉落了下来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x9,
        "#1263F#4P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x8,
        (
            "#1289F#5P她在被救出来的时候……\x01",
            "已经全身严重烧伤了。\x02\x03",

            "尽管如此，她仍然紧握\x01",
            "着那件首饰……\x02\x03",

            "金属部分虽然不行了，\x01",
            "不过石头的部分还安然无恙。\x02\x03",

            "#1290F就是这个。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x8, 0x2, 0x4, 0x320)
    Sleep(300)
    OP_99(0x8, 0x4, 0x7, 0x320)
    Sleep(500)

    ChrTalk(    #85
        0x9,
        "#1270F#4P……啊…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x8,
        (
            "#1290F#5P既不是七耀石也不是什么宝石，\x01",
            "只是一颗漂亮的石头。\x02\x03",

            "大概是在这附近的\x01",
            "小河里找到的吧。\x02\x03",

            "#1282F我怎么也想不通\x01",
            "她为什么要为了这样的东西……\x02\x03",

            "不过奇怪的是\x01",
            "我一点都不生她的气。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x8, 0x7, 0x9, 0x320)
    Sleep(500)

    ChrTalk(    #87
        0x8,
        (
            "#1289F#5P虽然我没什么留做纪念的意思……\x02\x03",

            "不过当战争结束我离开了村庄，\x01",
            "在外过着颓废的生活时，\x01",
            "也只有这件东西是我无法割舍的。\x02\x03",

            "#1290F哈哈……很丢人吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x9,
        "#1262F#4P没、没有……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x8,
        (
            "#1282F#5P真的是很丢人。\x02\x03",

            "看着这东西时，\x01",
            "我就能忘记愤怒。\x02\x03",

            "#1286F对没出息的我没能\x01",
            "救出米夏的那种愤怒……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x9,
        "#1265F#4P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x8,
        (
            "#1289F#5P通过把这种骚动的怒火\x01",
            "灌注在重剑上……\x02\x03",

            "总算我还没有\x01",
            "迷失自我。\x02\x03",

            "#1291F……在自我欺骗中\x01",
            "无法前进的废物……\x02\x03",

            "呵呵呵……\x01",
            "那个家伙没说错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x9,
        "#1263F#4P阿加特哥哥……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x8,
        (
            "#1280F#5P不……应该更加差劲。\x02\x03",

            "一个只知道闭目不看那些不想看的东西，\x01",
            "一味逃跑的白痴小子……\x02\x03",

            "是我最讨厌的丧家之犬。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #94
        0x8,
        "#1292F#5P#3S哈哈哈，这真是好笑！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #95
        0x9,
        (
            "#1263F#4P阿加特……哥哥……\x02\x03",

            "#1271F………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)

    def lambda_2407():
        OP_6D(-26900, 0, 47740, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2407)
    OP_8E(0x9, 0xFFFF9AA2, 0x0, 0xB644, 0x1F4, 0x0)
    SetChrPos(0x9, -26500, 0, 46620, 270)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 3)
    SetChrSubChip(0x9, 48)
    OP_99(0x9, 0x30, 0x32, 0x3E8)
    OP_1D(0x76)
    Sleep(500)

    ChrTalk(    #96
        0x9,
        (
            "#1271F#4P我……\x01",
            "虽然不能完全理解\x01",
            "阿加特哥哥的心情……\x02\x03",

            "也不知道\x01",
            "你为什么痛苦……\x02\x03",

            "#1262F可是，有一句话我想\x01",
            "代替米夏姐姐说给你听。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x8, 0xA, 0xB, 0x3E8)

    ChrTalk(    #97
        0x8,
        "#1281F#5P……？\x02",
    )

    CloseMessageWindow()
    Fade(500)

    def lambda_2512():
        OP_6B(2700, 500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2512)
    OP_0D()

    ChrTalk(    #98
        0x9,
        (
            "#1268F#4P#3S……不要把我很喜欢\x01",
            "的哥哥看扁！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #99
        0x9,
        (
            "#1274F#4P你根本不了解我哥哥\x01",
            "身上的优点！\x02\x03",

            "我最了解\x01",
            "哥哥了！\x02\x03",

            "#1268F我不允许任何人\x01",
            "把他说得那么坏，\x01",
            "即便是他本人！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0xFFFFFF6A, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #100
        0x8,
        "#1284F#5P什……么…\x02",
    )

    CloseMessageWindow()

    def lambda_2611():
        OP_6D(-27000, 0, 47520, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2611)
    OP_99(0x9, 0x33, 0x37, 0x4B0)

    def lambda_2632():
        OP_99(0x9, 0x38, 0x3B, 0x4B0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2632)

    def lambda_2642():
        OP_99(0x8, 0x18, 0x1B, 0x4B0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2642)
    WaitChrThread(0x0, 0x1)
    Sleep(500)

    ChrTalk(    #101
        0x8,
        "#1281F#5P………啊…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x9,
        (
            "#1272F#4P虽然我可能不及\x01",
            "米夏姐姐……\x02\x03",

            "即便如此，我仍然知道很多\x01",
            "阿加特哥哥身上的优点。\x02\x03",

            "所以，听到你把自己说得那么坏\x01",
            "我感到很悲伤……\x02\x03",

            "阿加特哥哥\x01",
            "根本不了解自己，\x01",
            "想到这一点我就很生气……\x02\x03",

            "所以……所以……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x8,
        (
            "#1281F#5P…………………………………\x02\x03",

            "#1291F……哈哈……败给你了……\x02\x03",

            "#1290F用和米夏一样的口气\x01",
            "把我教训了一番……\x02\x03",

            "明明是个小鬼，\x01",
            "想不到这么聪明……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x9,
        (
            "#1274F#4P请、请别把我\x01",
            "当小孩子……\x02\x03",

            "我……我……\x02\x03",

            "#1272F真的很悲伤……\x01",
            "所以也很生气……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x8,
        (
            "#1290F#5P……是吗……\x02\x03",

            "#1291F…………………………………\x02\x03",

            "我根本不了解\x01",
            "我自己吗……\x02\x03",

            "……好像说的没错。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)

    def lambda_28B9():
        OP_6D(-26720, 0, 47740, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_28B9)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 7)
    SetChrSubChip(0x9, 0)
    SetChrSubChip(0x8, 0)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x20)
    SetChrPos(0x8, -26640, 0, 46620, 90)
    SetChrPos(0x9, -26070, 0, 46640, 270)
    SetChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(500)
    OP_99(0x8, 0x0, 0x4, 0x320)
    OP_99(0x8, 0x4, 0x2, 0x320)
    Sleep(500)

    ChrTalk(    #106
        0x9,
        "#1273F#4P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x8,
        (
            "#1290F#5P谢谢你，提妲。\x02\x03",

            "你提醒得对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x9,
        "#1266F#4P阿加特哥哥……\x02",
    )

    CloseMessageWindow()
    OP_99(0x8, 0x5, 0x6, 0x320)
    Sleep(500)

    ChrTalk(    #109
        0x8,
        (
            "#1282F#5P……用自己的尺度\x01",
            "来衡量自己是不行的。\x02\x03",

            "那么我就努力挣扎一下吧。\x02\x03",

            "有愤怒和悲哀都没关系……\x01",
            "在找到答案之前，要一直前进。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x8, 0x6, 0xB, 0x384)
    Sleep(500)

    ChrTalk(    #110
        0x8,
        (
            "#1290F#5P嘿嘿，这样的话……\x02\x03",

            "一直带着这东西的\x01",
            "意义也总有一天会浮现出来吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    Sleep(500)
    OP_22(0xD, 0x0, 0x64)
    Sleep(5500)
    ClearMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T1103   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_1742 end

    def Function_4_2AB7(): pass

    label("Function_4_2AB7")

    OP_8E(0xFE, 0xFFFF9AA2, 0x0, 0xB644, 0x3E8, 0x0)
    SetChrPos(0x9, -26500, 0, 46620, 270)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 3)
    SetChrSubChip(0x9, 32)
    Return()

    # Function_4_2AB7 end

    SaveToFile()

Try(main)
