from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1121   ._SN',
        MapName             = 'Bose',
        Location            = 'T1121.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '卢格兰老人',                           # 9
        '信',                                   # 10
        '梅贝尔市长',                           # 11
        '亚妮拉丝',                             # 12
        '',                                     # 13
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02380 ._CH',             # 00
        'ED6_DT27/CH03093 ._CH',             # 01
        'ED6_DT06/CH20021 ._CH',             # 02
        'ED6_DT07/CH02363 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH02380P._CP',             # 00
        'ED6_DT27/CH03093P._CP',             # 01
        'ED6_DT06/CH20021P._CP',             # 02
        'ED6_DT07/CH02363P._CP',             # 03
    )

    DeclNpc(
        X                   = 180,
        Z                   = 0,
        Y                   = 4400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 1966082,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_14A",          # 00, 0
        "Function_1_1B1",          # 01, 1
        "Function_2_1B2",          # 02, 2
        "Function_3_B3B",          # 03, 3
        "Function_4_B8A",          # 04, 4
        "Function_5_BB3",          # 05, 5
        "Function_6_F71",          # 06, 6
        "Function_7_2638",         # 07, 7
        "Function_8_2C54",         # 08, 8
    )


    def Function_0_14A(): pass

    label("Function_0_14A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_191")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_175")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 6)
    Jump("loc_191")

    label("loc_175")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_191")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)

    label("loc_191")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_1B0")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 8)

    label("loc_1B0")

    Return()

    # Function_0_14A end

    def Function_1_1B1(): pass

    label("Function_1_1B1")

    Return()

    # Function_1_1B1 end

    def Function_2_1B2(): pass

    label("Function_2_1B2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(27740, 200, -2390, 0)
    OP_67(0, 4900, -10000, 0)
    OP_6B(2480, 0)
    OP_6C(45000, 0)
    OP_6E(323, 0)
    SetChrChipByIndex(0x10A, 1)
    SetChrSubChip(0x10A, 0)
    SetChrFlags(0x10A, 0x4)
    SetChrPos(0x10A, 26740, 200, -3610, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 25400, 800, -3800, 0)
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #0
        (
            "\x07\x05柏斯支部所属游击士，\x01",
            "亚妮拉丝·艾尔菲德――\x02\x03",

            "由于在『辉之环』事件中的活跃表现\x01",
            "而晋升Ｄ级的她，\x01",
            "现在已是年轻游击士的希望之星。\x02\x03",

            "然而，突如其来的一封信\x01",
            "打破了这样一帆风顺的平静……\x02\x03",

            "慵懒的午后――\x01",
            "亚妮拉丝在协会独自一人\x01",
            "读着那白色的纸片。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    OP_1D(0xB)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #1
        0x10A,
        (
            "#810F#5P嗯……\x02\x03",

            "唔唔唔唔……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_389():
        OP_6D(28150, 0, 630, 2000)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_389)
    OP_43(0x10, 0x0, 0x0, 0x3)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x10A, 0x0)
    Sleep(200)

    ChrTalk(    #2
        0x10,
        (
            "#630F怎么了，亚妮拉丝。\x01",
            "发出那么奇怪的声音。\x02\x03",

            "难道又吃太多冰淇淋\x01",
            "把肚子吃坏了？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00◆亚妮拉丝望向卢格兰的方向。（扭头）\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #4
        0x10A,
        (
            "#810F哇哇！？\x01",
            "这是秘密啦。\x02\x03",

            "其实，\x01",
            "我收到了爷爷的信……\x02",
        )
    )

    Jump("loc_4C0")

    label("loc_4C0")

    CloseMessageWindow()

    def lambda_4C7():
        OP_6D(27760, 200, -1960, 2000)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_4C7)

    def lambda_4DF():
        OP_6B(2400, 2000)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_4DF)
    OP_43(0x10, 0x0, 0x0, 0x4)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x10A, 0x0)

    ChrTalk(    #5
        0x10,
        (
            "#630F#5P哦……\x02\x03",

            "我记得，\x01",
            "你的祖父是……\x02",
        )
    )

    Jump("loc_540")

    label("loc_540")

    CloseMessageWindow()

    ChrTalk(    #6
        0x10A,
        (
            "#810F嗯，\x01",
            "是很有名的剑术老师。\x02\x03",

            "虽然已经老态龙钟了，\x01",
            "但要是现在和他比试，\x01",
            "我还是会被当成小孩子耍。\x02",
        )
    )

    Jump("loc_5BC")

    label("loc_5BC")

    CloseMessageWindow()

    ChrTalk(    #7
        0x10,
        (
            "#630F#5P能够把现役游击士当孩子耍，\x01",
            "真是恐怖的高手啊。\x02\x03",

            "……那，你祖父有什么事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10A,
        (
            "#810F嗯，这个……\x01",
            "这就更令人吃惊了……\x02\x03",

            "上面写着\x01",
            "『去见卡西乌斯』……\x02",
        )
    )

    Jump("loc_684")

    label("loc_684")

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        (
            "#630F#5P卡西乌斯……？\x02\x03",

            "就是那个卡西乌斯准将？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10A,
        (
            "#810F是、是的……\x02\x03",

            "爷爷好像曾经是\x01",
            "卡西乌斯先生的\x01",
            "剑术师父……\x02\x03",

            "１０年前卡西乌斯先生\x01",
            "舍弃剑道的时候，\x01",
            "也曾经来打过招呼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        (
            "#630F#5P说到１０年前，\x01",
            "正值『百日战役』……\x02\x03",

            "卡西乌斯先生退役\x01",
            "转做游击士时的事吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10A,
        (
            "#810F对于卡西乌斯先生舍弃剑道，\x01",
            "爷爷似乎相当遗憾……\x02\x03",

            "趁着这次他回归军队，\x01",
            "就想要重新\x01",
            "确认他的想法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "#630F#5P唔，原来如此啊。\x02\x03",

            "真是在意外的地方\x01",
            "有意外的缘分啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10A,
        (
            "#810F确、确实是啊……\x02\x03",

            "啊，就是因为这个，\x01",
            "卢格兰爷爷。\x02\x03",

            "我有点事\x01",
            "想拜托您……\x02",
        )
    )

    Jump("loc_8F9")

    label("loc_8F9")

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        (
            "#630F#5P嗯，你想请假吧？\x02\x03",

            "既然有这样的原因，\x01",
            "你就随便休息吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10A,
        "#810F哇，是真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        (
            "#630F#5P只不过……\x02\x03",

            "要等你把公告板上的通缉魔兽\x01",
            "给我全部收拾了之后才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #18
        0x10A,
        (
            "#810F不、不会吧……！？\x02\x03",

            "不是还有\x01",
            "５件那么多吗！？\x02",
        )
    )

    Jump("loc_A35")

    label("loc_A35")

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        (
            "#630F#5P三天前因为肚子痛\x01",
            "而请病假的家伙还有什么好说的。\x02\x03",

            "而且原因居然是\x01",
            "因为想要附赠品\x01",
            "而吃太多的冰淇淋……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #20
        0x10A,
        (
            "#810F哇、哇哇！！？\x02\x03",

            "我、我知道了，\x01",
            "这个就别说啦！！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_20(0x3E8)
    Sleep(1000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/C3100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1B2 end

    def Function_3_B3B(): pass

    label("Function_3_B3B")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 25510, -1750, 5500, 0)

    def lambda_B62():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B62)
    OP_8E(0xFE, 0x70D0, 0x0, 0x14BE, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_3_B3B end

    def Function_4_B8A(): pass

    label("Function_4_B8A")

    OP_8E(0xFE, 0x684C, 0x0, 0x4F6, 0x9C4, 0x0)
    OP_8E(0xFE, 0x681A, 0x0, 0xFFFFF7F4, 0x9C4, 0x0)
    Return()

    # Function_4_B8A end

    def Function_5_BB3(): pass

    label("Function_5_BB3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(27220, 0, -2090, 0)
    OP_67(0, 5790, -10000, 0)
    OP_6B(2340, 0)
    OP_6C(45000, 0)
    OP_6E(327, 0)
    SetChrChipByIndex(0x10A, 1)
    SetChrSubChip(0x10A, 0)
    SetChrFlags(0x10A, 0x4)
    SetChrPos(0x10A, 26740, 200, -3610, 270)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 0)
    SetChrFlags(0x10, 0x4)
    SetChrPos(0x10, 25330, 0, -2450, 180)
    Sleep(100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "\x07\x05――就这样，爷爷。\x02\x03",

            "很遗憾，\x01",
            "卡西乌斯先生还是无意回归剑术。\x02\x03",

            "不过，\x01",
            "这次爷爷的信\x01",
            "让我也稍微体会到了剑之道的深奥之处。\x02\x03",

            "至今为止，\x01",
            "都只重视『快』和『强』等方面……\x02\x03",

            "但最重要的应该\x01",
            "是自己为何而挥剑\x01",
            "的这种心情――『魂』才对吧。\x02\x03",

            "为什么我一直赢不了爷爷，\x01",
            "今天我终于明白其中道理了。\x02\x03",

            "虽然是个不成器的弟子，\x01",
            "但今后我也会尽一切努力。\x02\x03",

            "即使您去了天国\x01",
            "也一定要保佑我哦。\x02",
        )
    )

    Jump("loc_E02")

    label("loc_E02")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #22
        0x10A,
        (
            "#810F#2P――我寄出了这样的信……\x02\x03",

            "结果爷爷\x01",
            "大发雷霆。\x02",
        )
    )

    Jump("loc_E68")

    label("loc_E68")

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #23
        0x10,
        "#630F#5P呃，最后那两行有点问题吧。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    Sleep(2000)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_E6(0x1, 0x0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xA, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F13")
    OP_28(0xA, 0x4, 0x20)
    OP_3E(0x590, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x00得到了\x1F\x90\x05\x07\x00。\x02",
    )

    Jump("loc_F12")

    label("loc_F12")

    CloseMessageWindow()

    label("loc_F13")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xA, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F59")
    OP_28(0xA, 0x4, 0x10)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    AddMira(5000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #25
        "\x07\x00得到了\x07\x02５０００米拉\x07\x00。\x02",
    )

    Jump("loc_F58")

    label("loc_F58")

    CloseMessageWindow()

    label("loc_F59")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M5502   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_5_BB3 end

    def Function_6_F71(): pass

    label("Function_6_F71")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(27740, 200, -2390, 0)
    OP_67(0, 4900, -10000, 0)
    OP_6B(2680, 0)
    OP_6C(45000, 0)
    OP_6E(323, 0)
    SetChrChipByIndex(0x10A, 1)
    SetChrSubChip(0x10A, 0)
    SetChrFlags(0x10A, 0x4)
    SetChrPos(0x10A, 26740, 200, -3610, 270)
    FadeToBright(2000, 0)
    OP_6B(2480, 2000)
    OP_0D()
    OP_62(0x10A, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10A)
    Sleep(500)

    ChrTalk(    #26
        0x10A,
        (
            "#818F#11P嗯嗯……\x02\x03",

            "#817F原来如此，原来如此……\x02\x03",

            "#814F……………………………\x02\x03",

            "#1311F……唉，\x01",
            "没想到居然会有这种事。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 25510, -1750, 5500, 0)

    NpcTalk(    #27
        0x10,
        "老人的声音",
        "#2P喂，亚妮拉丝。\x02",
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1111():
        OP_6D(28150, 0, 630, 2000)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_1111)
    OP_43(0x10, 0x0, 0x0, 0x3)
    SetChrSubChip(0x10A, 2)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x10A, 0x0)
    Sleep(500)

    ChrTalk(    #28
        0x10A,
        "#1310F#12P啊，卢格兰爷爷。\x02",
    )

    CloseMessageWindow()

    def lambda_116B():
        OP_6D(27760, 200, -1960, 2000)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_116B)

    def lambda_1183():
        OP_6B(2400, 2000)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1183)
    OP_43(0x10, 0x0, 0x0, 0x4)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x10A, 0x0)
    Sleep(300)

    ChrTalk(    #29
        0x10,
        (
            "#633F#5P怎么了。\x01",
            "有什么问题吗？\x02\x03",

            "也不看公告板\x01",
            "就跑到二楼来躲着……\x02\x03",

            "#632F该不会是，\x01",
            "吃太多冰淇淋弄坏肚子了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10A,
        (
            "#819F#12P怎、怎么会……\x01",
            "我又不是小孩子了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10,
        (
            "#633F#5P嗬，你还敢说。\x02\x03",

            "#631F那么上次\x01",
            "到底是谁来着？\x02\x03",

            "一大早就吃了三个冰淇淋，\x01",
            "然后还要麻烦思潘斯爷爷\x01",
            "调了药才治好……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #32
        0x10A,
        (
            "#1317F#12P哇哇！？\x02\x03",

            "那、那是秘密啦。\x02\x03",

            "#817F而且，\x01",
            "那只不过是我当准游击士时的事吧！\x02\x03",

            "#816F现在已经反省过，\x01",
            "早上绝对只吃\x01",
            "一个冰淇淋了！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #33
        0x10,
        (
            "#634F#5P呃，这个，\x01",
            "一大早吃冰淇淋本身就有点……\x02\x03",

            "#630F……唉，也罢。\x02\x03",

            "那么，\x01",
            "你从刚才开始就一直在干什么呢？\x02",
        )
    )

    Jump("loc_145C")

    label("loc_145C")

    CloseMessageWindow()

    ChrTalk(    #34
        0x10A,
        (
            "#1310F#12P啊，对了。\x02\x03",

            "#811F其实今天早上，\x01",
            "我收到了住在远方的\x01",
            "爷爷写来的信。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #35
        0x10,
        (
            "#633F#5P哦……\x02\x03",

            "说到你的祖父……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10A,
        (
            "#819F#12P嗯，是剑术的老师。\x02\x03",

            "#816F说到『八叶一刀流』的\x01",
            "云·卡法伊，\x01",
            "在行内可是赫赫有名的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10,
        (
            "#631F#5P唔，是啊。\x02\x03",

            "虽然在听你说之前，\x01",
            "我只知道他的名字而已……\x02\x03",

            "#630F不过我记得有一段时期，\x01",
            "他也在利贝尔住过吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10A,
        (
            "#814F#12P啊，是的，您知道得真详细。\x02\x03",

            "#1316F只是，\x01",
            "我也记不大清楚了。\x02\x03",

            "因为那好像\x01",
            "是我出生前后的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10,
        (
            "#634F#5P哦……\x01",
            "是那么久以前的事了吗。\x02\x03",

            "#630F那么，\x01",
            "你祖父现在身体还健朗吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x10A,
        (
            "#1314F#12P嗯嗯，\x01",
            "看样子还生龙活虎的呢。\x02\x03",

            "最后一次见面\x01",
            "是在一年前左右……\x02\x03",

            "#819F已经七十岁了，\x01",
            "跟我比试的时候\x01",
            "还能把我当小孩子耍。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10,
        (
            "#631F#5P嗬嗬，\x01",
            "能够把现役游击士当孩子耍，\x01",
            "真是恐怖的高手啊。\x02\x03",

            "#632F唔……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x10A,
        "#810F#12P？　怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10,
        (
            "#634F#5P哎呀，亚妮拉丝。\x01",
            "以前我就一直\x01",
            "有这样一个疑问……\x02\x03",

            "#630F你为什么\x01",
            "不去祖父门下？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x10A,
        "#814F#12P咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        (
            "#630F#5P就是说，\x01",
            "你既然有志走上剑之道……\x02\x03",

            "在祖父身边磨练技艺\x01",
            "不是最好的捷径吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10A,
        "#1317F#12P唔，这个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10,
        (
            "#633F#5P啊啊，没什么……\x01",
            "我多管闲事了。\x02\x03",

            "#634F抱歉啊。\x01",
            "你就当是老人说胡话，\x01",
            "听过就算了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x10A,
        (
            "#819F#12P不不，没这回事……！\x02\x03",

            "#816F您刚才说的\x01",
            "完全没有多管闲事。\x02\x03",

            "#813F卢格兰爷爷的话\x01",
            "确实有一定的道理。\x02\x03",

            "只是有些事情\x01",
            "比较难说清楚……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x10,
        "#633F#5P哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x10A,
        (
            "#1316F#12P我想知道更多更多\x01",
            "关于剑术的知识……\x01",
            "想要追求剑的真谛。\x02\x03",

            "为此，\x01",
            "在爷爷门下修行\x01",
            "确实可以说是捷径。\x02\x03",

            "#813F但是和我对待剑术一样，\x01",
            "我也想在游击士方面有所作为……\x01",
            "不，也许是更为甚之。\x02\x03",

            "#812F嗯～，所以……\x01",
            "不是想作为剑术家来学习剑术，\x01",
            "而是想作为游击士来学习剑术……\x02\x03",

            "#1316F嗯～……\x01",
            "果然还是说不清楚啊。\x02",
        )
    )

    Jump("loc_1BA1")

    label("loc_1BA1")

    CloseMessageWindow()

    ChrTalk(    #51
        0x10,
        (
            "#631F#5P不……虽然只是模模糊糊的，\x01",
            "但是大概明白你想说的事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10A,
        (
            "#1314F#12P嗯……\x01",
            "而且，\x01",
            "爷爷也跟我说了。\x02\x03",

            "#817F身形和技法……\x01",
            "这些技术上的东西\x01",
            "已经全部教给我了。\x02\x03",

            "能不能运用自如\x01",
            "以后就看我自己了。\x02\x03",

            "#816F从这个意义上来说，\x01",
            "我想也没有必要\x01",
            "继续在爷爷门下学习剑术了。\x02\x03",

            "#819F嘿嘿……话虽如此，\x01",
            "其实我一直都很担心\x01",
            "自己到底是不是在进步呢。\x02",
        )
    )

    Jump("loc_1D29")

    label("loc_1D29")

    CloseMessageWindow()

    ChrTalk(    #53
        0x10,
        (
            "#633F#5P嗯，原来如此啊……\x02\x03",

            "…………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10A,
        (
            "#1317F#12P哎，那个……\x01",
            "卢格兰爷爷？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10,
        (
            "#634F#5P不，没什么……\x02\x03",

            "#630F难得你这么\x01",
            "认真地说这些话，\x01",
            "真是让我觉得吃惊呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x10A,
        (
            "#1316F#12P什、什么啊～……\x02\x03",

            "#812F让我说这么多的\x01",
            "不是卢格兰爷爷你吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10,
        (
            "#631F#5P呵呵呵，\x01",
            "哪里，你说得很好哦。\x02\x03",

            "#630F对了对了，\x01",
            "那关键的信里\x01",
            "到底写了些什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x10A,
        (
            "#814F#12P啊，对了……\x02\x03",

            "#819F嗯，这个，\x01",
            "就更令人大吃一惊了……\x02\x03",

            "#1314F上面写着\x01",
            "『去见卡西乌斯』呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #59
        0x10,
        (
            "#633F#5P卡西乌斯……？\x02\x03",

            "就是指那个卡西乌斯？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x10A,
        (
            "#1316F#12P嗯，看来没错。\x02\x03",

            "#816F似乎以前爷爷\x01",
            "曾经被邀请担任\x01",
            "王国军训练的特别讲师……\x02\x03",

            "在那个时候好像\x01",
            "指导过卡西乌斯先生。\x02\x03",

            "#817F从那以来，\x01",
            "两人之间似乎\x01",
            "一直保持着师徒关系……\x02\x03",

            "#1314F１０年前，\x01",
            "卡西乌斯先生放弃剑术的时候\x01",
            "似乎还特地到爷爷那里拜访过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x10,
        (
            "#633F#5P１０年前……\x02\x03",

            "#634F正是卡西乌斯从军队退役\x01",
            "成为游击士时的时候嘛。\x02\x03",

            "#632F哦，然后呢……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10A,
        (
            "#819F#12P嗯，然后……\x01",
            "爷爷最近听说\x01",
            "卡西乌斯先生回归了军队……\x02\x03",

            "『或许有趁此机会\x01",
            "  重拾剑术的觉悟』――\x01",
            "爷爷似乎是这么考虑的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x10,
        (
            "#634F#5P嗯……\x02\x03",

            "#630F所以，\x01",
            "就拜托你直接\x01",
            "确认其真伪了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x10A,
        "#816F#12P嗯嗯，就是这个意思。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10,
        (
            "#630F#5P原来如此……\x02\x03",

            "#631F……不过，\x01",
            "真是在意外的地方有意外的缘分啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x10A,
        (
            "#819F#12P哈哈……确实啊。\x02\x03",

            "#816F对了，卢格兰爷爷。\x01",
            "就是因为这个。\x02\x03",

            "所以，\x01",
            "我想拜托您一件事……\x02",
        )
    )

    Jump("loc_231D")

    label("loc_231D")

    CloseMessageWindow()

    ChrTalk(    #67
        0x10,
        (
            "#631F#5P嗯，你想请假吧？\x02\x03",

            "既然有这样的原因就没问题啊。\x02\x03",

            "而且，我也可以帮你\x01",
            "安排和卡西乌斯的见面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x10A,
        "#1310F#12P哇，是真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x10,
        (
            "#634F#5P嗯，\x01",
            "尽情把心中的疑问弄个明白吧。\x02\x03",

            "#630F只不过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x10A,
        "#814F#12P只不过……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x10,
        (
            "#631F#5P要等你把现在公告板上的通缉魔兽\x01",
            "给我全部收拾了之后才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #72
        0x10A,
        (
            "#1317F#12P不、不会吧……！？\x02\x03",

            "我记得\x01",
            "还有五件任务的啊！？\x02",
        )
    )

    Jump("loc_24EE")

    label("loc_24EE")

    CloseMessageWindow()

    ChrTalk(    #73
        0x10,
        (
            "#631F#5P这有什么，消灭附近的魔兽\x01",
            "对现在的你来说还不是小菜一碟。\x02\x03",

            "#630F而且卢安那边\x01",
            "借走的库拉茨\x01",
            "也还没回来。\x02\x03",

            "该做的事\x01",
            "你要给我好好做才行啊。\x02",
        )
    )

    Jump("loc_25A2")

    label("loc_25A2")

    CloseMessageWindow()

    ChrTalk(    #74
        0x10A,
        "#1316F#12P呜呜呜……是～。\x02",
    )

    CloseMessageWindow()

    def lambda_25D0():
        OP_6B(2700, 3000)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_25D0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #75
        "\x07\x00三天之后——\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_A2(0x2505)
    NewScene("ED6_DT21/C3100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_F71 end

    def Function_7_2638(): pass

    label("Function_7_2638")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(1240, 0, 4560, 0)
    OP_67(0, 5550, -10000, 0)
    OP_6B(2520, 0)
    OP_6C(45000, 0)
    OP_6E(327, 0)
    SetChrPos(0x10A, 0, 0, 2340, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 180, 0, 4400, 180)

    def lambda_26AE():
        OP_6B(2320, 2000)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_26AE)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #76
        0x10,
        (
            "#631F#5P……是吗。\x01",
            "真是不错的经历啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x10A,
        (
            "#819F#12P是……\x02\x03",

            "#1314F说不定爷爷\x01",
            "正是知道会有这样的事\x01",
            "才会写那封信给我的吧。\x02\x03",

            "因为我上次给他\x01",
            "写信的时候写了一些\x01",
            "打退堂鼓的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x10,
        (
            "#634F#5P原来如此……\x01",
            "不愧是卡西乌斯的师父啊。\x02\x03",

            "#630F对了，虽然你刚回来，\x01",
            "不过还是得请你去解决\x01",
            "休假时积攒起来的委托。\x02\x03",

            "在你离开的这段时间，\x01",
            "还有市长亲自提出的委托呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x10A,
        "#1317F#12P呃……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x10,
        (
            "#631F#5P呵呵……\x01",
            "这不是正好吗。\x02\x03",

            "让自己摆脱武器束缚的\x01",
            "训练机会这么快就来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10A,
        (
            "#819F#12P哈哈……\x01",
            "确实是这样呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2905():
        OP_6B(2220, 3000)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_2905)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #82
        "\x07\x0C#40W――就这样，爷爷。\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(    #83
        (
            "\x07\x0C#40W我想您应该一开始就知道了，\x01",
            "卡西乌斯先生还是\x01",
            "无意回归剑之道。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(    #84
        (
            "\x07\x0C#40W不过，这次爷爷的信\x01",
            "让我也重新认识了自己的剑术。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(    #85
        (
            "\x07\x0C#40W至今为止我只重视\x01",
            "『速度』和『力量』那些方面……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(    #86
        (
            "\x07\x0C#40W但是比起这些，\x01",
            "最重要的应该是『自己为何而挥剑』\x01",
            "的那种『理念』――也就是『灵魂』才对吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(    #87
        (
            "\x07\x0C#40W为什么一直赢不了爷爷，\x01",
            "我终于明白其中道理了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(    #88
        (
            "\x07\x0C#40W虽然我是个不成器的弟子，\x01",
            "但今后也会尽一切努力。\x01",
            "　　　　　　　　　　　　　亚妮拉丝敬上。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    CloseMessageWindow()
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #89
        "\x07\x00Episode『剑之道』　～Fin～\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_E6(0x1, 0x0)
    OP_C2(0x1, 0x0)
    Call(6, 25)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xA, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 6)), scpexpr(EXPR_END)), "loc_2BF6")
    OP_28(0xA, 0x4, 0x20)
    OP_3E(0x590, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #90
        "\x07\x00得到了\x1F\x90\x05\x07\x00。\x02",
    )

    Jump("loc_2BF5")

    label("loc_2BF5")

    CloseMessageWindow()

    label("loc_2BF6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xA, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C3C")
    OP_28(0xA, 0x4, 0x10)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    AddMira(5000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #91
        "\x07\x00得到了\x07\x02５０００米拉\x07\x00。\x02",
    )

    Jump("loc_2C3B")

    label("loc_2C3B")

    CloseMessageWindow()

    label("loc_2C3C")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M5502   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_7_2638 end

    def Function_8_2C54(): pass

    label("Function_8_2C54")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(27170, 0, -2020, 0)
    OP_67(0, 5100, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(323, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x12, 26740, 200, -3610, 270)
    SetChrPos(0x13, 24060, 200, -3580, 90)
    FadeToBright(2000, 0)
    OP_6B(2500, 2000)
    OP_0D()
    Sleep(500)

    ChrTalk(    #92
        0x13,
        (
            "#1317F#6P呃，那个～梅贝尔市长……\x02\x03",

            "#819F能不能再……\x01",
            "仔细说一下委托内容？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x12,
        (
            "#615F#11P咳、咳咳……\x02\x03",

            "#618F就是说，那个……\x01",
            "他、他们两个是什么关系……\x02\x03",

            "#612F以及对方是怎样的人，\x01",
            "都要麻烦你调查一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x13,
        (
            "#1316F#6P嗯～也就是说……\x02\x03",

            "调查两人交往的真伪\x01",
            "和对方的品性……\x02\x03",

            "#812F就是这两方面对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x12,
        (
            "#615F#11P嗯、嗯嗯，就是这样。\x02\x03",

            "#612F有、有什么问题吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x13,
        (
            "#1316F#6P……………………………\x02\x03",

            "#813F那个……梅贝尔市长……\x02\x03",

            "#1314F我们游击士\x01",
            "的确也可以接受\x01",
            "调查品性之类的委托……\x02\x03",

            "不过那纯粹只是\x01",
            "和犯罪有关的情况。\x02\x03",

            "否则的话，\x01",
            "就会和侵犯隐私权\x01",
            "挂上钩啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x12,
        "#613F#11P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x13,
        (
            "#817F#6P莉拉小姐所交往的男性\x01",
            "可能会图谋不轨……\x02\x03",

            "#812F是否有这样的征兆呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x12,
        (
            "#618F#11P不、不是……\x02\x03",

            "看起来倒是个\x01",
            "善良又诚实的男人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x13,
        (
            "#1316F#6P嗯、嗯……\x02\x03",

            "#1314F确实，\x01",
            "也不能光靠外表来判断\x01",
            "一个人的人品……\x02\x03",

            "不过现在就要游击士\x01",
            "出动实在有点……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x12,
        (
            "#615F#11P是、是吗……\x01",
            "确实如你所说呢……\x02\x03",

            "#610F……我明白了。\x01",
            "我会另想办法的。\x02\x03",

            "#617F亚妮拉丝小姐，很抱歉。\x01",
            "刚才的话就当没说过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x13,
        (
            "#1317F#6P唔，嗯……\x02\x03",

            "#819F……那个。\x01",
            "市长应该是想支持\x01",
            "莉拉小姐的恋爱吧？\x02\x03",

            "既然如此，为什么还这么担心呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x12,
        "#615F#11P………………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x12)
    Sleep(500)

    ChrTalk(    #104
        0x12,
        (
            "#618F#11P你应该也知道她的事……\x01",
            "莉拉在『百日战役』的时候\x01",
            "失去了双亲。\x02\x03",

            "当时她心灵的伤痛……\x01",
            "或许现在也没有消失。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #105
        0x13,
        "#1317F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x12,
        (
            "#615F#11P……就我所知，\x01",
            "这种事对莉拉而言\x01",
            "也是第一次经历。\x02\x03",

            "所以就更加……\x01",
            "我一定不能\x01",
            "让她受到伤害。\x02\x03",

            "#618F对方的家世和财产……\x01",
            "这些东西都无所谓。\x02\x03",

            "他是否真的\x01",
            "能给莉拉幸福……\x02\x03",

            "#610F我只是……\x01",
            "想确定这个而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x13,
        "#813F#6P市长……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x12,
        (
            "#617F#11P……所以，\x01",
            "我似乎有些失去冷静了。\x02\x03",

            "#611F不过既然是莉拉，\x01",
            "总有一天会把对方的事\x01",
            "告诉我的吧。\x02\x03",

            "到时候\x01",
            "我再直接去问本人吧。\x02",
        )
    )

    Jump("loc_34B7")

    label("loc_34B7")

    CloseMessageWindow()

    ChrTalk(    #109
        0x13,
        (
            "#817F#6P不……\x01",
            "用不着那样了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x12,
        "#613F#11P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x13,
        (
            "#816F#6P市长的心情\x01",
            "我完～全了解了！\x02\x03",

            "#815F在下亚妮拉丝·艾尔菲德！\x01",
            "请让我接受之前的委托！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)
    OP_62(0x12, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)

    ChrTalk(    #112
        0x12,
        (
            "#618F#11P但、但是……\x02\x03",

            "#612F真的可以吗？\x01",
            "游击士不是有规定……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x13,
        (
            "#816F#6P没问题！\x01",
            "规定的解释在某种程度上，\x01",
            "是因每个游击士而异的啦！\x02\x03",

            "#1316F被规定所束缚\x01",
            "而忽视了人心的话，\x01",
            "那就是本末倒置了……\x02\x03",

            "#1310F市长的父母心，\x01",
            "要是随便归于侵犯隐私的层次\x01",
            "就太草率了！\x02\x03",

            "#811F请您放一百个心，\x01",
            "交给我就行了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x12,
        (
            "#611F#11P亚妮拉丝小姐……\x02\x03",

            "#617F……谢谢你。\x01",
            "听你这么说\x01",
            "我真是放心多了。\x02\x03",

            "#610F对方的隐私\x01",
            "不必过于追究……\x02\x03",

            "请以此为前提\x01",
            "展开调查可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x13,
        (
            "#816F#6P嗯嗯，交给我吧！\x02\x03",

            "#819F嘿嘿，莉拉小姐的恋爱……\x01",
            "要是能进展顺利就好了呢！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3808():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3808)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    Sleep(500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #116
        (
            "\x07\x00#40W――就这样，\x01",
            "亚妮拉丝接受了梅贝尔市长的委托，\x01",
            "马上开始调查两人的情况。\x02\x03",

            "为了不让他们本人发现，\x01",
            "她小心谨慎地\x01",
            "开始收集旁人的证言……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T1131   ._SN", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_8_2C54 end

    SaveToFile()

Try(main)
