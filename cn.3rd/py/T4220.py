from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4220   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4220.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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
        '艾莉茜雅女王',                         # 9
        '杜南公爵',                             # 10
        '艾南',                                 # 11
        '奥利维特皇子',                         # 12
        '穆拉少校',                             # 13
        '科洛蒂娅公主',                         # 14
        '卡西乌斯准将',                         # 15
        '尤莉亚上尉',                           # 16
        '奥斯本宰相',                           # 17
        '希尔丹夫人',                           # 18
        '雷克特书记官',                         # 19
        '亲卫队队员',                           # 20
        '亲卫队队员',                           # 21
        '亲卫队队员',                           # 22
        '亲卫队队员',                           # 23
        '亲卫队队员',                           # 24
        '亲卫队队员',                           # 25
        '亲卫队队员',                           # 26
        '亲卫队队员',                           # 27
        '亲卫队队员',                           # 28
        '亲卫队队员',                           # 29
        '亲卫队队员',                           # 30
        '亲卫队队员',                           # 31
        '目标用照相机',                         # 32
        '艾莉茜雅女王',                         # 33
        '奥利维特皇子',                         # 34
        '穆拉少校',                             # 35
        '科洛蒂娅公主',                         # 36
        '卡西乌斯准将',                         # 37
        '奥斯本宰相',                           # 38
        '雷克特书记官',                         # 39
        '希尔丹夫人',                           # 40
        '',                                     # 41
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
        'ED6_DT07/CH02010 ._CH',             # 00
        'ED6_DT07/CH02140 ._CH',             # 01
        'ED6_DT07/CH02580 ._CH',             # 02
        'ED6_DT27/CH03260 ._CH',             # 03
        'ED6_DT27/CH03570 ._CH',             # 04
        'ED6_DT27/CH03960 ._CH',             # 05
        'ED6_DT27/CH03670 ._CH',             # 06
        'ED6_DT07/CH02090 ._CH',             # 07
        'ED6_DT27/CH03950 ._CH',             # 08
        'ED6_DT06/CH20129 ._CH',             # 09
        'ED6_DT07/CH01320 ._CH',             # 0A
        'ED6_DT07/CH02460 ._CH',             # 0B
        'ED6_DT26/CH20805 ._CH',             # 0C
        'ED6_DT26/CH20808 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH02010P._CP',             # 00
        'ED6_DT07/CH02140P._CP',             # 01
        'ED6_DT07/CH02580P._CP',             # 02
        'ED6_DT27/CH03260P._CP',             # 03
        'ED6_DT27/CH03570P._CP',             # 04
        'ED6_DT27/CH03960P._CP',             # 05
        'ED6_DT27/CH03670P._CP',             # 06
        'ED6_DT07/CH02090P._CP',             # 07
        'ED6_DT27/CH03950P._CP',             # 08
        'ED6_DT06/CH20129P._CP',             # 09
        'ED6_DT07/CH01320P._CP',             # 0A
        'ED6_DT07/CH02460P._CP',             # 0B
        'ED6_DT26/CH20805P._CP',             # 0C
        'ED6_DT26/CH20808P._CP',             # 0D
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x80,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_51A",          # 00, 0
        "Function_1_56B",          # 01, 1
        "Function_2_56C",          # 02, 2
        "Function_3_10A8",         # 03, 3
    )


    def Function_0_51A(): pass

    label("Function_0_51A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_542")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_542")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_542")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_56A")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)

    label("loc_56A")

    Return()

    # Function_0_51A end

    def Function_1_56B(): pass

    label("Function_1_56B")

    Return()

    # Function_1_56B end

    def Function_2_56C(): pass

    label("Function_2_56C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(2000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00『异变』平息后约两个月……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(800)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 500, 154350, 180)
    SetChrPos(0x10E, 0, 0, 149740, 0)
    OP_6D(200, 0, 133360, 0)
    OP_67(0, 6820, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(318, 0)

    def lambda_631():
        OP_6D(1660, 200, 153680, 6000)
        ExitThread()

    QueueWorkItem(0x27, 0, lambda_631)

    def lambda_649():
        OP_67(0, 4059, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_649)

    def lambda_661():
        OP_6B(2800, 6000)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_661)

    def lambda_671():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x27, 3, lambda_671)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x27, 0x0)
    Sleep(500)

    NpcTalk(    #1
        0x10E,
        "尤莉亚上尉",
        (
            "#178F────以上就是\x01",
            "关于『异变』的\x01",
            "详细报告。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        (
            "#094F尤莉亚上尉，\x01",
            "你做的很出色。\x02\x03",

            "#90F为那样巨大的混乱划下终止符，\x01",
            "给国家重新带来光明，\x01",
            "我从心底感谢你。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #3
        0x10E,
        "尤莉亚上尉",
        (
            "#176F陛下…………\x02\x03",

            "#176F您的夸奖\x01",
            "在下实在不敢当……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "#090F不，我是作为全体民众的代表\x01",
            "向你表示感谢的。\x02\x03",

            "#090F你为了『异变』后各地的重建工作\x01",
            "仍然在到处奔波。\x02\x03",

            "我听说你领导的亲卫队\x01",
            "现在工作十分繁忙，\x01",
            "所以就想慰劳一下。\x02\x03",

            "#090F真的是辛苦你了。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #5
        0x10E,
        "尤莉亚上尉",
        (
            "#170F是………\x01",
            "非常感谢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "#090F对你功劳的表彰，\x01",
            "之后会挑选合适的时间\x01",
            "在正式场合下进行。\x02\x03",

            "#91F呵呵，\x01",
            "摩尔根将军强力推荐你升职，\x01",
            "我个人也很期待呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #7
        0x10E,
        "尤莉亚上尉",
        (
            "#172F陛、陛下，\x01",
            "这样实在…………\x02\x03",

            "#178F这次的事件能够得到解决，\x01",
            "是很多人努力的结果。\x02\x03",

            "我自己所做的\x01",
            "只不过是非常微不足道的事。\x02\x03",

            "#175F所以，实在不敢接受\x01",
            "表彰和升职这样的奖赏……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        (
            "#094F……尤莉亚上尉。\x02\x03",

            "正如你所说的，\x01",
            "能够阻止『异变』的发生\x01",
            "的确是很多人努力的结果。\x02\x03",

            "战斗的人，守护重要事物的人，\x01",
            "坚持着渡过困难的人，\x01",
            "大家都为『异变』的平息做出了贡献。\x02\x03",

            "#090F但是，如果没有埃尔赛尤号这只翅膀，\x01",
            "事情显然无法得到解决。\x02\x03",

            "率领这只翅膀的……\x01",
            "尤莉亚上尉，就是你啊。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #9
        0x10E,
        "尤莉亚上尉",
        (
            "#175F可、可是……\x01",
            "表彰暂且不说，\x01",
            "升职实在不敢接受。\x02\x03",

            "我就任上尉的时间\x01",
            "本来就还不长，\x01",
            "再被委以重任的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        (
            "#090F呵呵，\x01",
            "不必过于谦虚。\x02\x03",

            "我知道比起为自己考虑，\x01",
            "你更愿意脚踏实地完成工作。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #11
        0x10,
        (
            "#094F…………对了……\x02\x03",

            "#090F尤莉亚上尉，\x01",
            "今天你去休假一天，\x01",
            "怎么样啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #12
        0x10E,
        "尤莉亚上尉",
        (
            "#173F啊…………？\x01",
            "休假……是吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "#090F嗯，比起刚才严肃的话题，\x01",
            "这是我个人对你\x01",
            "表示的感谢。\x02\x03",

            "上尉你每天都要\x01",
            "往返奔波于军队司令部\x01",
            "和格兰赛尔城之间。\x02\x03",

            "亲卫队员们\x01",
            "也曾经向我说起\x01",
            "希望你能够休息一下的事情呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    NpcTalk(    #14
        0x10E,
        "尤莉亚上尉",
        (
            "#172F实、实在抱歉。\x02\x03",

            "这些话本不该\x01",
            "让陛下听到的……\x02\x03",

            "#176F（是勒克司还是利昂呢……）\x02\x03",

            "（每次和那两个人见面，\x01",
            "  都要听她们啰嗦『上尉，\x01",
            "  请休息一下吧』之类的话……！）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        (
            "#090F……尤莉亚上尉，\x01",
            "今天你就别工作了，\x01",
            "好好休息一天吧。\x02\x03",

            "然后，\x01",
            "希望你明天能够带着\x01",
            "崭新的心情继续工作。\x02",
        )
    )

    Jump("loc_F54")

    label("loc_F54")

    CloseMessageWindow()

    NpcTalk(    #16
        0x10E,
        "尤莉亚上尉",
        (
            "#172F是、是的…………\x02\x03",

            "#176F……我明白了。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_6D(200500, 0, 149240, 0)
    OP_67(0, 4960, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(135000, 0)
    OP_6E(280, 0)
    SetChrPos(0x10, 200000, 500, 154350, 180)
    SetChrPos(0x10E, 200000, 0, 149740, 0)
    OP_0D()
    Sleep(100)

    def lambda_100F():
        OP_6B(2700, 400)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_100F)
    SetChrChipByIndex(0x10E, 9)
    SetChrSubChip(0x10E, 0)
    OP_99(0x10E, 0x0, 0x1, 0x5DC)
    Sleep(600)

    NpcTalk(    #17
        0x10E,
        "尤莉亚上尉",
        (
            "#170F#5P王室亲卫队大队长尤莉亚·舒华兹，\x01",
            "今天休假一天。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1086():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0x27, 0, lambda_1086)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4210   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_56C end

    def Function_3_10A8(): pass

    label("Function_3_10A8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x10, 0, 500, 154350, 180)
    SetChrPos(0x15, -1400, 500, 154070, 180)
    SetChrPos(0x16, 1090, 500, 152800, 180)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x13, -200, 0, 148930, 0)
    SetChrPos(0x14, 630, 0, 147940, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x1B, 2200, 0, 142260, 270)
    SetChrPos(0x1C, 2200, 0, 140760, 270)
    SetChrPos(0x1D, 2200, 0, 139260, 270)
    SetChrPos(0x1E, 3300, 0, 142260, 270)
    SetChrPos(0x1F, 3300, 0, 140760, 270)
    SetChrPos(0x20, 3300, 0, 139260, 270)
    SetChrPos(0x21, -2200, 0, 142260, 90)
    SetChrPos(0x22, -2200, 0, 140760, 90)
    SetChrPos(0x23, -2200, 0, 139260, 90)
    SetChrPos(0x24, -3300, 0, 142260, 90)
    SetChrPos(0x25, -3300, 0, 140760, 90)
    SetChrPos(0x26, -3300, 0, 139260, 90)
    OP_6D(1940, 0, 136940, 0)
    OP_67(0, 3640, -10000, 0)
    OP_6B(3660, 0)
    OP_6C(45000, 0)
    OP_6E(366, 0)

    def lambda_1281():
        OP_6D(1940, 0, 153520, 6000)
        ExitThread()

    QueueWorkItem(0x27, 0, lambda_1281)

    def lambda_1299():
        OP_67(0, 5140, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_1299)
    FadeToBright(3000, 0)
    OP_0D()
    WaitChrThread(0x27, 0x0)
    Sleep(500)
    Fade(1000)
    OP_6D(1410, 250, 152950, 0)
    OP_67(0, 4070, -10000, 0)
    OP_6B(2790, 0)
    OP_6C(45000, 0)
    OP_6E(317, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #18
        0x13,
        (
            "#1545F#12P──女王陛下、王太女殿下。\x01",
            "至今为止承蒙你们多方照顾了。\x02\x03",

            "#1540F连我想搭乘『埃尔赛尤号』\x01",
            "回国的无理愿望也能够满足，\x01",
            "实在是有些过意不去……\x02\x03",

            "#1541F今日之恩，\x01",
            "日后必将涌泉相报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        (
            "#091F#5P呵呵，您太客气了。\x02\x03",

            "#090F用『埃尔赛尤号』送\x01",
            "像殿下这样的国宾，\x01",
            "也是理所应当的事情。\x02\x03",

            "我们也受到了殿下\x01",
            "各种各样的帮助呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x15,
        (
            "#1818F#5P如果有机会的话，\x01",
            "请一定要再次拜访利贝尔。\x02\x03",

            "到那时，\x01",
            "艾丝蒂尔他们也应该回来了……\x02\x03",

            "我们会为你们办一场\x01",
            "盛大的欢迎会的。\x02",
        )
    )

    Jump("loc_1519")

    label("loc_1519")

    CloseMessageWindow()

    ChrTalk(    #21
        0x13,
        (
            "#1541F#12P哈哈，真是万分期待。\x02\x03",

            "#1540F这么说来，艾丝蒂尔他们\x01",
            "也差不多该出发了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x16,
        (
            "#1125F#5P还没有，现在他们\x01",
            "还在洛连特做旅行的准备。\x02\x03",

            "#1120F等他们出发的时候，\x01",
            "我也会请假去送行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x13,
        (
            "#1545F#12P是这样啊……\x02\x03",

            "#1540F现在哈梅尔遗迹仍然被封锁着，\x01",
            "不过我会负责安排\x01",
            "让他们能够进入。\x02\x03",

            "请代我向他们两人问好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x16,
        (
            "#1125F#5P……知道了。\x02\x03",

            "皇子殿下，十分感谢您。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x13,
        (
            "#1541F#12P没什么，\x01",
            "与他们给我的帮助比起来，\x01",
            "这些小事不值一提。\x02\x03",

            "#1540F──卡西乌斯先生，\x01",
            "也要向您表示感谢。\x02\x03",

            "如果没有您的协助，\x01",
            "帝国军队的师团\x01",
            "是不会那么容易撤退的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x16,
        (
            "#1120F#5P呵呵……\x01",
            "这是我要说的话才对。\x02\x03",

            "#1125F还有……\x01",
            "我想你也应该清楚，\x01",
            "这种情况都在对方的预料之内。\x02\x03",

            "#1122F对那个『铁血宰相』来说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x13,
        "#1545F#12P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x15,
        "#1814F#5P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "#093F#5P……说的没错。\x02\x03",

            "#094F实际上，\x01",
            "在那种情况下压制利贝尔\x01",
            "对埃雷波尼亚没有什么好处。\x02\x03",

            "但他们却依然开发了\x01",
            "公认效率低下的蒸汽战车。\x02\x03",

            "#092F唯一的可能性就是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x13,
        (
            "#1551F#12P……为了让其它国家知道，\x01",
            "即使发生导力停止现象，\x01",
            "帝国军队也仍然能够行动。\x02\x03",

            "#1542F恐怕这才是他真正的目的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #31
        0x15,
        "#1813F#5P啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x16,
        (
            "#1125F#5P的确……\x01",
            "分析得十分精辟。\x02\x03",

            "#1122F所谓『导力停止现象』\x01",
            "对各国来说仍然是不可理解的现象。\x02\x03",

            "今后说不定会在\x01",
            "其它地方再次发生，\x01",
            "也可能永远都不会再发生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x14,
        (
            "#272F#11P……其实，\x01",
            "竣工的蒸汽战车只有少数几辆。\x02\x03",

            "#276F只是在莱恩福尔特社的\x01",
            "生产车间中用普通的\x01",
            "导力战车零件拼凑起来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x13,
        (
            "#1545F#12P也就是说，\x01",
            "现在只有帝国掌握着制造工艺。\x02\x03",

            "而在情况不明朗的情况下，\x01",
            "其它国家也没有余力\x01",
            "引入效率低下的蒸汽武器。\x02\x03",

            "#1540F──造成的结果就是，\x01",
            "帝国军队的潜在威慑能力\x01",
            "会得到进一步提升……\x02\x03",

            "#1541F简直就是把战争作为\x01",
            "外交道具来使用啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x15,
        (
            "#1813F#5P居然是这样……\x02\x03",

            "#1819F……果然，\x01",
            "我还差得很远啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x13,
        (
            "#1544F#12P这种情况下，\x01",
            "该是说那位宰相大人非比寻常吧。\x02\x03",

            "#1542F好坏暂且不提，\x01",
            "他的这种思路已经超前于时代了。\x02\x03",

            "#1541F哼，\x01",
            "向这样难缠的对手挑战，\x01",
            "我也真是够无谋的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x15,
        "#1872F#5P殿下……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x14,
        (
            "#274F#11P真是的……\x01",
            "干嘛说得事不关己似的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10,
        (
            "#094F#5P……现在您应当专注于\x01",
            "巩固自身的立足之处。\x02\x03",

            "#090F但是，请千万要小心。\x02\x03",

            "一定不要迷失\x01",
            "自己本应持有的立场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x13,
        (
            "#1545F#12P……我明白了。\x02\x03",

            "#1540F如果因此就失态的话，\x01",
            "请您特地用『埃尔赛尤号』\x01",
            "送我回帝都就失去意义了。\x02\x03",

            "承您所言，必将铭记于心。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -500, 0, 138900, 0)

    NpcTalk(    #41
        0x19,
        "女性的声音",
        "#1P失、失礼了……！\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1FA2():

        label("loc_1FA2")

        TurnDirection(0xFE, 0x19, 500)
        OP_48()
        Jump("loc_1FA2")

    QueueWorkItem2(0x13, 2, lambda_1FA2)
    Sleep(50)

    def lambda_1FB8():

        label("loc_1FB8")

        TurnDirection(0xFE, 0x19, 500)
        OP_48()
        Jump("loc_1FB8")

    QueueWorkItem2(0x14, 2, lambda_1FB8)

    def lambda_1FC9():
        OP_6D(1510, 250, 152250, 2500)
        ExitThread()

    QueueWorkItem(0x27, 0, lambda_1FC9)

    def lambda_1FE1():
        OP_67(0, 3740, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_1FE1)

    def lambda_1FF9():
        OP_6B(3000, 2500)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_1FF9)

    def lambda_2009():
        OP_8E(0xFE, 0xFFFFFE0C, 0x0, 0x23E9C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2009)
    WaitChrThread(0x19, 0x1)
    OP_44(0x13, 0x2)
    OP_44(0x14, 0x2)
    Sleep(500)

    ChrTalk(    #42
        0x15,
        "#1814F#5P希尔丹夫人……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10,
        (
            "#097F#5P女官长，发生什么事了？\x02\x03",

            "你这么惊慌失措，\x01",
            "可真是不常见啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x19,
        (
            "#716F#12P……很抱歉。\x01",
            "就在刚才，\x01",
            "有不速之客前来拜访格兰赛尔城。\x02\x03",

            "#714F因为实在太过意外了，\x01",
            "所以不吝做出打断谈话的失礼举动\x01",
            "也要通报给陛下及诸位知道……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        "#093F#5P不速之客……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x13,
        (
            "#1540F#5P唔，\x01",
            "那么我们也该告辞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x19,
        (
            "#716F不，那个……\x02\x03",

            "#714F不仅是对陛下，\x01",
            "那位来客也想对\x01",
            "皇子殿下进行问候。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #48
        0x14,
        "#273F#5P什么……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x13,
        (
            "#1543F#5P………………………………\x02\x03",

            "#1542F希尔丹夫人。\x01",
            "那位客人的名字是？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x19,
        (
            "#713F#12P……是。\x02\x03",

            "#710F他报上的名字是，\x01",
            "埃雷波尼亚帝国宰相\x01",
            "吉利亚斯·奥斯本。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2F, 0x80)
    SetChrPos(0x28, 0, 500, 154350, 180)
    SetChrPos(0x2B, -1400, 500, 154070, 180)
    SetChrPos(0x2C, 201090, 500, 152800, 180)
    SetChrPos(0x29, 2140, 0, 149660, 225)
    SetChrPos(0x2A, 3000, 0, 148560, 225)
    SetChrPos(0x2F, -3380, 0, 148560, 135)
    SetChrPos(0x10, 200000, 500, 154350, 180)
    SetChrPos(0x15, 198600, 500, 154070, 180)
    SetChrPos(0x16, 201090, 500, 152800, 180)
    SetChrPos(0x19, 196620, 0, 150160, 135)
    SetChrPos(0x13, 202140, 0, 149660, 225)
    SetChrPos(0x14, 203000, 0, 148560, 225)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x18, 200000, 0, 126680, 0)
    SetChrPos(0x1A, 199200, 0, 126680, 0)
    OP_9F(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    SetChrPos(0x2D, 0, 0, 126680, 0)
    SetChrPos(0x2E, -800, 0, 126680, 0)
    OP_9F(0x2D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(0, 0, 137500, 0)
    OP_67(0, 5560, -10000, 0)
    OP_6B(3220, 0)
    OP_6C(45000, 0)
    OP_6E(338, 0)
    OP_6D(1940, 0, 136940, 0)
    OP_67(0, 3640, -10000, 0)
    OP_6B(3660, 0)
    OP_6C(45000, 0)
    OP_6E(366, 0)
    OP_1D(0x74)
    Sleep(500)
    FadeToBright(1000, 0)

    def lambda_2526():
        OP_6D(1940, 0, 153520, 8000)
        ExitThread()

    QueueWorkItem(0x27, 0, lambda_2526)

    def lambda_253E():
        OP_67(0, 5140, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_253E)

    def lambda_2556():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_2556)

    def lambda_2568():
        OP_8E(0xFE, 0x30D40, 0x0, 0x2394C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_2568)

    def lambda_2583():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_2583)

    def lambda_2595():
        OP_8E(0xFE, 0x0, 0x0, 0x2394C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_2595)
    Sleep(500)

    def lambda_25B5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_25B5)

    def lambda_25C7():
        OP_8E(0xFE, 0x30A20, 0x0, 0x2317C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_25C7)

    def lambda_25E2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_25E2)

    def lambda_25F4():
        OP_8E(0xFE, 0xFFFFFCE0, 0x0, 0x2317C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_25F4)
    Sleep(5000)
    Fade(500)
    OP_44(0x27, 0xFF)
    OP_6D(200060, 0, 142400, 0)
    OP_67(0, 4920, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(180000, 0)
    OP_6E(280, 0)

    def lambda_265A():
        OP_8E(0xFE, 0x30D40, 0x0, 0x2394C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_265A)

    def lambda_2675():
        OP_8E(0xFE, 0x30A20, 0x0, 0x2317C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2675)
    SetChrPos(0x1B, 202200, 0, 142260, 270)
    SetChrPos(0x1C, 202200, 0, 140760, 270)
    SetChrPos(0x1D, 202200, 0, 139260, 270)
    SetChrPos(0x1E, 203300, 0, 142260, 270)
    SetChrPos(0x1F, 203300, 0, 140760, 270)
    SetChrPos(0x20, 203300, 0, 139260, 270)
    SetChrPos(0x21, 197800, 0, 142260, 90)
    SetChrPos(0x22, 197800, 0, 140760, 90)
    SetChrPos(0x23, 197800, 0, 139260, 90)
    SetChrPos(0x24, 196700, 0, 142260, 90)
    SetChrPos(0x25, 196700, 0, 140760, 90)
    SetChrPos(0x26, 196700, 0, 139260, 90)

    def lambda_275C():
        OP_6D(200060, 0, 145750, 2000)
        ExitThread()

    QueueWorkItem(0x27, 0, lambda_275C)

    def lambda_2774():
        OP_67(0, 3810, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_2774)
    WaitChrThread(0x27, 0x0)
    WaitChrThread(0x18, 0x1)
    Sleep(500)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x200, 0x5A, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x200, 0xFFFFFF, 0x0, "C_VIS354._CH")
    OP_C6(0x0, 0x0, 140000, 0, 500)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("奥斯本宰相")

    AnonymousTalk(    #51
        (
            "——初次见面。\x02\x03",

            "本人是埃雷波尼亚帝国政府代表，\x01",
            "吉利亚斯·奥斯本。\x02\x03",

            "以如此形式冒昧来访，\x01",
            "请务必见谅。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 250, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_C7(0x1, 0xFF, 0x0)
    Sleep(500)

    ChrTalk(    #52
        0x10,
        "#097F#6P……您就是………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x15,
        "#1814F#4P…………………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x18, 45, 400)
    Sleep(300)

    ChrTalk(    #54
        0x18,
        (
            "#1485F#11P还有，\x01",
            "我们亲爱的奥利维特皇子殿下……\x02\x03",

            "#1480F很久不见了。\x01",
            "自上次一别大概有一年了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x13,
        (
            "#1545F#6P……啊，大概是吧。\x02\x03",

            "#1542F可是，宰相。\x01",
            "我有些无法理解……\x02\x03",

            "为何你身为一国宰相\x01",
            "竟然不事先知会就来拜访这里？\x02\x03",

            "能不能把原委\x01",
            "解释清楚呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x18,
        (
            "#1483F#11P真是抱歉了……\x02\x03",

            "#1485F其实之前到东部各州\x01",
            "进行视察工作的进展\x01",
            "比预想的要顺利。\x02\x03",

            "#1480F由于得到了一些空闲，\x01",
            "于是我就来这里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x13,
        "#1543F#6P哎呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x18,
        (
            "#1485F#11P本来我应该像\x01",
            "殿下您一样\x01",
            "在『异变』发生时赶来的……\x02\x03",

            "但当时却因为要应对\x01",
            "南部混乱的局势而作罢。\x02\x03",

            "#1480F现在终于能够抽出时间，\x01",
            "因此不假思索地便前来拜访了。\x02\x03",

            "请原谅我事先未曾通报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x13,
        (
            "#1545F#6P……原来如此。\x01",
            "这也是事出非常。\x02\x03",

            "#1540F不用顾忌我了，\x01",
            "赶快向女王陛下致礼吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x18,
        (
            "#1485F#11P十分感谢。\x01",
            "那么……\x02",
        )
    )

    Jump("loc_2C4F")

    label("loc_2C4F")

    CloseMessageWindow()
    Sleep(150)
    OP_8C(0x18, 0, 400)
    Sleep(300)

    def lambda_2C67():
        OP_6D(201240, 100, 149300, 2000)
        ExitThread()

    QueueWorkItem(0x27, 0, lambda_2C67)

    def lambda_2C7F():
        OP_67(0, 4920, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_2C7F)

    def lambda_2C97():
        OP_6C(142000, 2000)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_2C97)

    def lambda_2CA7():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0x27, 3, lambda_2CA7)

    def lambda_2CB7():

        label("loc_2CB7")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_2CB7")

    QueueWorkItem2(0x14, 2, lambda_2CB7)

    def lambda_2CC8():
        OP_8E(0xFE, 0x30D40, 0x0, 0x247FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_2CC8)
    Sleep(200)

    def lambda_2CE8():
        OP_8E(0xFE, 0x30868, 0x0, 0x24540, 0x8FC, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2CE8)
    Sleep(400)

    def lambda_2D08():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2D08)
    Sleep(100)

    def lambda_2D1B():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_2D1B)
    WaitChrThread(0x18, 0x1)
    WaitChrThread(0x1A, 0x1)
    Sleep(500)
    Fade(100)
    SetChrChipByIndex(0x18, 13)
    SetChrSubChip(0x18, 0)
    OP_22(0x8F, 0x0, 0x64)
    OP_99(0x18, 0x0, 0x5, 0x3E8)
    Sleep(500)

    ChrTalk(    #61
        0x18,
        (
            "#1485F#11P……重新正式拜会一次。\x02\x03",

            "艾莉茜雅女王陛下，\x01",
            "科洛蒂娅王太女殿下，\x01",
            "谨祝万安。\x02\x03",

            "#1482F这次异变事件，\x01",
            "对贵国来说真是一场严峻的考验。\x02\x03",

            "#1484F请允许我在此表达衷心的慰问……\x01",
            "以及对异变顺利得到平息的\x01",
            "祝贺之情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x15,
        (
            "#1813F#6P………啊…………\x02\x03",

            "#1815F您如此郑重多礼，实在不胜惶恐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x10,
        (
            "#094F#6P相对而言，\x01",
            "异变竟然影响到了贵国南部，\x01",
            "也让我们感到有所愧疚及不安。\x02\x03",

            "不仅如此，\x01",
            "还烦劳宰相阁下亲自到访……\x02\x03",

            "#090F请接受我衷心的\x01",
            "感谢及歉意。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_99(0x18, 0x6, 0x7, 0x3E8)
    SetChrChipByIndex(0x18, 8)
    SetChrSubChip(0x18, 0)
    Sleep(500)

    ChrTalk(    #64
        0x18,
        (
            "#1480F#11P没什么，据说异变的背后隐藏着\x01",
            "某个蠢蠢欲动的神秘组织。\x02\x03",

            "原先我对此毫无知晓，\x01",
            "只抱着想支援贵国的心情而出动了军队，\x01",
            "实是太过愚蠢和轻率。\x02\x03",

            "#1485F也因此受到了\x01",
            "皇帝陛下的斥责。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10,
        "#097F#6P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x18,
        (
            "#1480F#11P不过，\x01",
            "由于奥利维特殿下的活跃，\x01",
            "本人失态所造成的损失也算得到了弥补……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x18, 90, 400)
    Sleep(500)

    ChrTalk(    #67
        0x18,
        (
            "#1485F#12P……我也要对殿下表达\x01",
            "衷心的感谢之情才是。\x02\x03",

            "#1480F此外，也辛苦您\x01",
            "见证了此次异变的平息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x13,
        (
            "#1545F#5P没什么……\x01",
            "我只是略尽绵薄之力而已。\x02\x03",

            "#1540F并且我还得到了\x01",
            "陛下、殿下以及\x01",
            "这位卡西乌斯准将的诸多帮助。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x18, 0, 400)
    Sleep(300)

    ChrTalk(    #69
        0x18,
        "#1483F#11P哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x16,
        (
            "#1125F#6P……初次见面。\x02\x03",

            "#1120F在下是利贝尔王国军队准将，\x01",
            "卡西乌斯·布莱特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x18,
        (
            "#1485F#11P呵呵，\x01",
            "您在我们帝国也是鼎鼎大名啊。\x02\x03",

            "#1480F能见到您真是荣幸。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x16,
        (
            "#1120F#6P彼此彼此……\x01",
            "能被著名的奥斯本大人赏识\x01",
            "我也感到十分荣幸。\x02\x03",

            "#1123F不过，没想到宰相阁下\x01",
            "会有如此大胆的行动力……\x02\x03",

            "#1122F看来有必要重新\x01",
            "对阁下进行评价了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x18,
        (
            "#1485F#11P没什么，我也十分惊叹于\x01",
            "异变发生时王国军的应对措施呢。\x02\x03",

            "能够灵活应对各种事态的\x01",
            "柔中带刚的组织运用……\x02\x03",

            "#1481F对于庞大而笨重的我军来说，\x01",
            "真是遥不可及的理想形态啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x16,
        (
            "#1125F#6P哈哈，您过谦了。\x02\x03",

            "#1120F据说著名的帝国军情报局\x01",
            "正是阁下亲自领导的……\x02\x03",

            "对于当务之急为重建情报部门的我军来说，\x01",
            "对此也是羡慕之极啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x18,
        (
            "#1486F#11P哈哈……\x01",
            "我们彼此都对所欠缺之物有怨念吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x16,
        "#1121F#6P哈哈，说的没错呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x13,
        (
            "#1551F#5P……话说回来，宰相。\x01",
            "之后你有什么打算？\x02\x03",

            "#1540F很不凑巧\x01",
            "我今天就要离开利贝尔了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x18, 90, 400)
    Sleep(300)

    ChrTalk(    #78
        0x18,
        (
            "#1485F#12P嗯，我已经知道了。\x02\x03",

            "#1480F听说您要搭乘著名的\x01",
            "『埃尔赛尤号』凯旋回国……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x13,
        "#1542F#5P……不愧是您，消息真灵通啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x18,
        (
            "#1485F#12P如果我也能同乘的话……\x01",
            "其实我本来想这么请求的……\x02\x03",

            "#1480F不过遗憾的是\x01",
            "之后我还有其它安排。\x02\x03",

            "和殿下您不同，\x01",
            "我过了中午就必须要出发了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10,
        (
            "#097F#6P哎呀……\x01",
            "我本来还打算请你们\x01",
            "今晚留在这里用餐的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x18,
        (
            "#1486F#12P哈哈，不劳您烦心了。\x02\x03",

            "我冒昧来访，\x01",
            "实在担当不起丰盛的招待。\x02\x03",

            "#1485F不过，\x01",
            "离船到来还有一段时间……\x02\x03",

            "如果可以的话，\x01",
            "能占用殿下您一点时间吗？\x02\x03",

            "#1481F……我有很多话\x01",
            "想私下与您交流一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x14,
        "#270F#5P………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x1A,
        "#1885F#11P……………呵……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x15,
        "#1813F#6P…………………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x13)
    Sleep(500)

    ChrTalk(    #86
        0x13,
        (
            "#1545F#5P……是吗，好啊。\x02\x03",

            "#1540F我也正想和您\x01",
            "好好谈一次呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x18,
        "#1485F#12P呵呵，那还真是凑巧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x10,
        (
            "#094F#6P……如果可以的话，\x01",
            "我来为你们安排房间吧。\x02\x03",

            "#090F女官长，拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x19,
        "#713F#12P……遵命。\x02",
    )

    CloseMessageWindow()

    def lambda_39C8():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_39C8)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4221   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_10A8 end

    SaveToFile()

Try(main)
