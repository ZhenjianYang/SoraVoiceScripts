from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4110   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        '西加罗',                               # 9
        '芭蒂',                                 # 10
        '拉尔夫',                               # 11
        '比尔爷爷',                             # 12
        '伊鲁妮婆婆',                           # 13
        '丹克',                                 # 14
        '梅洛涅',                               # 15
        '贝斯卡',                               # 16
        '',                                     # 17
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
        'ED6_DT07/CH01030 ._CH',             # 00
        'ED6_DT07/CH01043 ._CH',             # 01
        'ED6_DT07/CH01040 ._CH',             # 02
        'ED6_DT07/CH01490 ._CH',             # 03
        'ED6_DT07/CH01180 ._CH',             # 04
        'ED6_DT07/CH01460 ._CH',             # 05
        'ED6_DT07/CH01140 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH01030P._CP',             # 00
        'ED6_DT07/CH01043P._CP',             # 01
        'ED6_DT07/CH01040P._CP',             # 02
        'ED6_DT07/CH01490P._CP',             # 03
        'ED6_DT07/CH01180P._CP',             # 04
        'ED6_DT07/CH01460P._CP',             # 05
        'ED6_DT07/CH01140P._CP',             # 06
    )

    DeclNpc(
        X                   = 7220,
        Z                   = 200,
        Y                   = 53570,
        Direction           = 269,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -29600,
        Z                   = 4000,
        Y                   = 1830,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -27310,
        Z                   = 0,
        Y                   = -4370,
        Direction           = 81,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 26900,
        Z                   = 4000,
        Y                   = -470,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 26830,
        Z                   = 4000,
        Y                   = -1620,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 91740,
        Z                   = 0,
        Y                   = -1110,
        Direction           = 23,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 51810,
        Z                   = 0,
        Y                   = 56250,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 51250,
        Z                   = 0,
        Y                   = 55180,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )


    ScpFunction(
        "Function_0_1E2",          # 00, 0
        "Function_1_1F9",          # 01, 1
        "Function_2_203",          # 02, 2
        "Function_3_227",          # 03, 3
        "Function_4_39B",          # 04, 4
        "Function_5_56F",          # 05, 5
        "Function_6_625",          # 06, 6
        "Function_7_733",          # 07, 7
        "Function_8_814",          # 08, 8
        "Function_9_920",          # 09, 9
        "Function_10_A12",         # 0A, 10
    )


    def Function_0_1E2(): pass

    label("Function_0_1E2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F8")
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0x14, 0x10)

    label("loc_1F8")

    Return()

    # Function_0_1E2 end

    def Function_1_1F9(): pass

    label("Function_1_1F9")

    OP_B1("t4110_n")
    Return()

    # Function_1_1F9 end

    def Function_2_203(): pass

    label("Function_2_203")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_226")
    OP_8D(0xFE, -30880, 4000, -29430, 0, 2000)
    Jump("Function_2_203")

    label("loc_226")

    Return()

    # Function_2_203 end

    def Function_3_227(): pass

    label("Function_3_227")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_234")
    Jump("loc_397")

    label("loc_234")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_2F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_290")

    ChrTalk(    #0
        0xFE,
        (
            "我那么说了之后，\x01",
            "他就在王都买了房子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "我真是倍受宠爱啊～㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EF")

    label("loc_290")


    ChrTalk(    #2
        0xFE,
        (
            "说要住在大都市的\x01",
            "是我啦。\x02",
        )
    )

    Jump("loc_2BC")

    label("loc_2BC")

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "因为是难得的新居嘛。\x01",
            "要心满意足才行呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_2EF")

    Jump("loc_397")

    label("loc_2F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_2FC")
    Jump("loc_397")

    label("loc_2FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_397")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_341")

    ChrTalk(    #4
        0xFE,
        "嗯，大都市真是好啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "买东西也很方便。\x02",
    )

    CloseMessageWindow()
    Jump("loc_397")

    label("loc_341")


    ChrTalk(    #6
        0xFE,
        (
            "嘻嘻，\x01",
            "我缠着老公买了房子呢㈱\x02",
        )
    )

    Jump("loc_36E")

    label("loc_36E")

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "住在王都，\x01",
            "是不是比较浪漫呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_397")

    TalkEnd(0xFE)
    Return()

    # Function_3_227 end

    def Function_4_39B(): pass

    label("Function_4_39B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_3A8")
    Jump("loc_56B")

    label("loc_3A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_4AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_426")

    ChrTalk(    #8
        0xFE,
        (
            "总感觉这好像是\x01",
            "拿妻子的任性\x01",
            "没办法的结果。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "今天也是，\x01",
            "把家务都推给我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "这样好吗……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4AB")

    label("loc_426")


    ChrTalk(    #11
        0xFE,
        (
            "最近房地产的价格\x01",
            "也上涨了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "虽然我也觉得\x01",
            "是买房的时候了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "可总感觉这好像是\x01",
            "拿妻子的任性\x01",
            "没办法的结果……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_4AB")

    Jump("loc_56B")

    label("loc_4AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_4B8")
    Jump("loc_56B")

    label("loc_4B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_56B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_512")

    ChrTalk(    #14
        0xFE,
        (
            "一忍不住\x01",
            "就买下了这栋房子呢。\x02",
        )
    )

    Jump("loc_4F6")

    label("loc_4F6")

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "…………好贵啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_56B")

    label("loc_512")


    ChrTalk(    #16
        0xFE,
        "怎样，不错的房子吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "我们买下来了哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "………………一忍不住就……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_56B")

    TalkEnd(0xFE)
    Return()

    # Function_4_39B end

    def Function_5_56F(): pass

    label("Function_5_56F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_57C")
    Jump("loc_621")

    label("loc_57C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_5CD")

    ChrTalk(    #19
        0xFE,
        (
            "老太婆啊，\x01",
            "差不多该去艾尔贝离宫了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "那里最适合散步了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_621")

    label("loc_5CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_5D7")
    Jump("loc_621")

    label("loc_5D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_621")

    ChrTalk(    #21
        0xFE,
        "啊啊，天气真好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "今天也是\x01",
            "平静的一天呢。\x02",
        )
    )

    Jump("loc_620")

    label("loc_620")

    CloseMessageWindow()

    label("loc_621")

    TalkEnd(0xFE)
    Return()

    # Function_5_56F end

    def Function_6_625(): pass

    label("Function_6_625")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_632")
    Jump("loc_72F")

    label("loc_632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_68B")

    ChrTalk(    #23
        0xFE,
        (
            "嗯嗯，\x01",
            "那个地方很漂亮的。\x02",
        )
    )

    Jump("loc_662")

    label("loc_662")

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "不过老头子，\x01",
            "你可别太勉强哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72F")

    label("loc_68B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_695")
    Jump("loc_72F")

    label("loc_695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_72F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_70C")

    ChrTalk(    #25
        0xFE,
        (
            "能从那场战争灾祸中恢复过来，\x01",
            "都是多亏了女王陛下啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "我从内心\x01",
            "对她充满感激。\x02",
        )
    )

    Jump("loc_708")

    label("loc_708")

    CloseMessageWindow()
    Jump("loc_72F")

    label("loc_70C")


    ChrTalk(    #27
        0xFE,
        "嗯嗯，和平是最重要的了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_72F")

    TalkEnd(0xFE)
    Return()

    # Function_6_625 end

    def Function_7_733(): pass

    label("Function_7_733")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_7F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_790")

    ChrTalk(    #28
        0xFE,
        "我在港口工作哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "今天天气很好，\x01",
            "说不定可以看见海市蜃楼哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F2")

    label("loc_790")

    OP_8C(0xFE, 23, 0)

    ChrTalk(    #30
        0xFE,
        (
            "好～\x01",
            "房子漏水的地方也修好了……\x02",
        )
    )

    Jump("loc_7C3")

    label("loc_7C3")

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "嘿～\x01",
            "今天也要打起精神干活啊！\x02",
        )
    )

    Jump("loc_7EE")

    label("loc_7EE")

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_7F2")

    Jump("loc_810")

    label("loc_7F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_7FF")
    Jump("loc_810")

    label("loc_7FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_809")
    Jump("loc_810")

    label("loc_809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_810")

    label("loc_810")

    TalkEnd(0xFE)
    Return()

    # Function_7_733 end

    def Function_8_814(): pass

    label("Function_8_814")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_901")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_8A2")

    ChrTalk(    #32
        0xFE,
        (
            "很快就该到\x01",
            "大主教大人讲话的时间了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "大主教大人的讲话，\x01",
            "可真让人受益匪浅啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "你们也一起来听听怎么样？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8FE")

    label("loc_8A2")


    ChrTalk(    #35
        0xFE,
        (
            "哎呀，很快就该到\x01",
            "大主教大人讲话的时间了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "要赶快\x01",
            "去大圣堂才行呢。\x02",
        )
    )

    Jump("loc_8FA")

    label("loc_8FA")

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_8FE")

    Jump("loc_91C")

    label("loc_901")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_90B")
    Jump("loc_91C")

    label("loc_90B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_915")
    Jump("loc_91C")

    label("loc_915")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_91C")

    label("loc_91C")

    TalkEnd(0xFE)
    Return()

    # Function_8_814 end

    def Function_9_920(): pass

    label("Function_9_920")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_9F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_993")

    ChrTalk(    #37
        0xFE,
        (
            "看，\x01",
            "这个是很有前途的品种吧？\x02",
        )
    )

    Jump("loc_95B")

    label("loc_95B")

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "啊啊，\x01",
            "真想借个真正的农场做实验啊。\x02",
        )
    )

    Jump("loc_98F")

    label("loc_98F")

    CloseMessageWindow()
    Jump("loc_9F0")

    label("loc_993")


    ChrTalk(    #39
        0xFE,
        (
            "我正在研究\x01",
            "农作物的栽培技术。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "……话虽如此，\x01",
            "也只不过是凭兴趣随便弄弄而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_9F0")

    Jump("loc_A0E")

    label("loc_9F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_9FD")
    Jump("loc_A0E")

    label("loc_9FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_A07")
    Jump("loc_A0E")

    label("loc_A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_A0E")

    label("loc_A0E")

    TalkEnd(0xFE)
    Return()

    # Function_9_920 end

    def Function_10_A12(): pass

    label("Function_10_A12")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_B08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_A78")

    ChrTalk(    #41
        0xFE,
        (
            "因为我喜欢过\x01",
            "被绿色围绕的生活嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "……能和这个人在一起\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B05")

    label("loc_A78")


    ChrTalk(    #43
        0xFE,
        (
            "呵呵，\x01",
            "我丈夫兴趣很奇怪吧？\x02",
        )
    )

    Jump("loc_AA3")

    label("loc_AA3")

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "不过我觉得\x01",
            "那是个很不错的兴趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "因为，\x01",
            "被绿色围绕的生活，\x01",
            "不是很棒吗？\x02",
        )
    )

    Jump("loc_B01")

    label("loc_B01")

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_B05")

    Jump("loc_B23")

    label("loc_B08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_B12")
    Jump("loc_B23")

    label("loc_B12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_B1C")
    Jump("loc_B23")

    label("loc_B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_B23")

    label("loc_B23")

    TalkEnd(0xFE)
    Return()

    # Function_10_A12 end

    SaveToFile()

Try(main)
