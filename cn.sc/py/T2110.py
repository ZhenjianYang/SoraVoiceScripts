from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2110   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
        '布丽奇特',                             # 9
        '贝尔夫',                               # 10
        '希艾尔',                               # 11
        '爱蕾塔',                               # 12
        '连茨',                                 # 13
        '丽泽',                                 # 14
        '托尼奥',                               # 15
        '诺莉雅',                               # 16
        '路易',                                 # 17
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
        'ED6_DT07/CH01230 ._CH',             # 00
        'ED6_DT07/CH01140 ._CH',             # 01
        'ED6_DT07/CH01540 ._CH',             # 02
        'ED6_DT07/CH01170 ._CH',             # 03
        'ED6_DT07/CH01460 ._CH',             # 04
        'ED6_DT07/CH01030 ._CH',             # 05
        'ED6_DT07/CH01040 ._CH',             # 06
        'ED6_DT07/CH01690 ._CH',             # 07
        'ED6_DT07/CH01470 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH01230P._CP',             # 00
        'ED6_DT07/CH01140P._CP',             # 01
        'ED6_DT07/CH01540P._CP',             # 02
        'ED6_DT07/CH01170P._CP',             # 03
        'ED6_DT07/CH01460P._CP',             # 04
        'ED6_DT07/CH01030P._CP',             # 05
        'ED6_DT07/CH01040P._CP',             # 06
        'ED6_DT07/CH01690P._CP',             # 07
        'ED6_DT07/CH01470P._CP',             # 08
    )

    DeclNpc(
        X                   = 24980,
        Z                   = 0,
        Y                   = 62760,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -28000,
        Z                   = 0,
        Y                   = 61400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 1950,
        Z                   = 0,
        Y                   = 5470,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -470,
        Z                   = 0,
        Y                   = 1090,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 23690,
        Z                   = 0,
        Y                   = 4490,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 27150,
        Z                   = 0,
        Y                   = -1550,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 26000,
        Z                   = 4000,
        Y                   = -510,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -5740,
        Z                   = 0,
        Y                   = 35100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 5430,
        Z                   = 0,
        Y                   = 64750,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )


    ScpFunction(
        "Function_0_212",          # 00, 0
        "Function_1_303",          # 01, 1
        "Function_2_304",          # 02, 2
        "Function_3_31A",          # 03, 3
        "Function_4_33E",          # 04, 4
        "Function_5_362",          # 05, 5
        "Function_6_52D",          # 06, 6
        "Function_7_A14",          # 07, 7
        "Function_8_ECC",          # 08, 8
        "Function_9_1345",         # 09, 9
        "Function_10_1610",        # 0A, 10
        "Function_11_1806",        # 0B, 11
        "Function_12_1D61",        # 0C, 12
        "Function_13_2242",        # 0D, 13
        "Function_14_24A0",        # 0E, 14
        "Function_15_2BF1",        # 0F, 15
        "Function_16_2C35",        # 10, 16
        "Function_17_2C79",        # 11, 17
        "Function_18_46AC",        # 12, 18
    )


    def Function_0_212(): pass

    label("Function_0_212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_232")
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xD, 27250, 0, -1740, 87)
    Jump("loc_2A8")

    label("loc_232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_24B")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_2A8")

    label("loc_24B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_27F")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xA, 1700, 0, 2029, 90)
    Jump("loc_2A8")

    label("loc_27F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_28E")
    SetChrFlags(0xC, 0x80)
    Jump("loc_2A8")

    label("loc_28E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_29C")
    Jump("loc_2A8")

    label("loc_29C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_2A8")
    SetChrFlags(0xC, 0x80)

    label("loc_2A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 0)), scpexpr(EXPR_END)), "loc_2B7")
    ClearChrFlags(0x9, 0x10)
    Jump("loc_2DE")

    label("loc_2B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 7)), scpexpr(EXPR_END)), "loc_2D2")
    SetChrPos(0x8, -230, 0, 63820, 270)
    Jump("loc_2DE")

    label("loc_2D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_2DE")
    SetChrFlags(0x9, 0x10)

    label("loc_2DE")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (107, "loc_2EA"),
        (SWITCH_DEFAULT, "loc_302"),
    )


    label("loc_2EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2FF")
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_2FF")

    Jump("loc_302")

    label("loc_302")

    Return()

    # Function_0_212 end

    def Function_1_303(): pass

    label("Function_1_303")

    Return()

    # Function_1_303 end

    def Function_2_304(): pass

    label("Function_2_304")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_319")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_304")

    label("loc_319")

    Return()

    # Function_2_304 end

    def Function_3_31A(): pass

    label("Function_3_31A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_33D")
    OP_8D(0xFE, -6630, 65280, -3270, 67330, 1000)
    Jump("Function_3_31A")

    label("loc_33D")

    Return()

    # Function_3_31A end

    def Function_4_33E(): pass

    label("Function_4_33E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_361")
    OP_8D(0xFE, -2620, 970, 1167, -2110, 3000)
    Jump("Function_4_33E")

    label("loc_361")

    Return()

    # Function_4_33E end

    def Function_5_362(): pass

    label("Function_5_362")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_40D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CD")

    ChrTalk(    #0
        0xFE,
        (
            "哥哥他说要帮\x01",
            "爸爸的忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "哥哥也在努力啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "我也要努力帮妈妈的忙哦！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_40A")

    label("loc_3CD")


    ChrTalk(    #3
        0xFE,
        (
            "哥哥他说要帮\x01",
            "爸爸的忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "我也要努力帮妈妈的忙哦！\x02",
    )

    CloseMessageWindow()

    label("loc_40A")

    Jump("loc_529")

    label("loc_40D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_471")

    ChrTalk(    #5
        0xFE,
        (
            "导力器停止了\x01",
            "爸爸的工作也很受影响呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "但是，我爸爸很厉害。\x01",
            "一定会马上修好的吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_529")

    label("loc_471")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_4B3")

    ChrTalk(    #7
        0xFE,
        (
            "我哥哥\x01",
            "已经开始工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "好像在帮\x01",
            "爸爸的忙呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_529")

    label("loc_4B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_4BD")
    Jump("loc_529")

    label("loc_4BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4F0")

    ChrTalk(    #9
        0xFE,
        (
            "爸爸这次\x01",
            "因为选举一直不在家呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_529")

    label("loc_4F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_529")

    ChrTalk(    #10
        0xFE,
        (
            "哥哥，\x01",
            "都不跟我玩～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "好难得\x01",
            "才回家一次～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_529")

    TalkEnd(0xFE)
    Return()

    # Function_5_362 end

    def Function_6_52D(): pass

    label("Function_6_52D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_65A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F5")

    ChrTalk(    #12
        0xFE,
        (
            "虽然是传言，\x01",
            "听说学院出了事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "不过，我儿子罗基克\x01",
            "应该没事吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "那家伙意外的谨慎，\x01",
            "应该早早的就逃出去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "比起勇敢的孩子，胆小的孩子\x01",
            "反而更能让父母安心呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_657")

    label("loc_5F5")


    ChrTalk(    #16
        0xFE,
        (
            "虽说学院好像出了事，\x01",
            "我儿子罗基克应该没事的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "那家伙意外的谨慎，\x01",
            "应该早早的就逃出去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_657")

    Jump("loc_A10")

    label("loc_65A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_770")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_719")

    ChrTalk(    #18
        0xFE,
        (
            "因为导力器停止了，\x01",
            "港湾区那边一片混乱啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "我先生被市长一大清早\x01",
            "叫出去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "即使在选举中输了，\x01",
            "为了那家伙还是尽心尽力啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "我先生\x01",
            "真是个没心机的老好人。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_76D")

    label("loc_719")


    ChrTalk(    #22
        0xFE,
        (
            "因为导力器停止了，\x01",
            "港湾区那边一片混乱啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "我先生被市长一大清早\x01",
            "叫出去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76D")

    Jump("loc_A10")

    label("loc_770")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_7D6")

    ChrTalk(    #24
        0xFE,
        (
            "过几天我去先生\x01",
            "工作的地方看望他一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "不去鞭策他一下\x01",
            "马上就会说出没出息的话了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A10")

    label("loc_7D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_835")

    ChrTalk(    #26
        0xFE,
        (
            "好像是支持者之间\x01",
            "发生了争执呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "既然是我先生，\x01",
            "肯定是打算阻止\x01",
            "又没成功吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A10")

    label("loc_835")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_90B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_89A")

    ChrTalk(    #28
        0xFE,
        (
            "我儿子罗基克\x01",
            "什么事情都喜欢讲道理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "什么事都是一堆理论，\x01",
            "真让我头疼。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_908")

    label("loc_89A")

    OP_A2(0x5)

    ChrTalk(    #30
        0xFE,
        (
            "说起来，王立学院\x01",
            "马上就要放长假了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "那儿子一整天\x01",
            "都要待在家里了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "呼，想想\x01",
            "都觉得头疼了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_908")

    Jump("loc_A10")

    label("loc_90B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_A10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_982")

    ChrTalk(    #33
        0xFE,
        (
            "我先生就算当了市长候选人\x01",
            "还是那么没出息啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "想知道他什么样子，\x01",
            "就出去看看外面的墙壁就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A10")

    label("loc_982")

    OP_A2(0x5)

    ChrTalk(    #35
        0xFE,
        (
            "我先生就算当了市长候选人\x01",
            "还是那么没出息啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "换句话说就是『胆量不够』。\x01",
            "事到如今说话还打颤。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "支持者们都看着，\x01",
            "不能振作点吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A10")

    TalkEnd(0xFE)
    Return()

    # Function_6_52D end

    def Function_7_A14(): pass

    label("Function_7_A14")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_AD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A96")

    ChrTalk(    #38
        0xFE,
        "这次是学院事件吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "利贝尔王国到底\x01",
            "怎么回事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "入学考试能不能照预定\x01",
            "进行，心里很不安啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_AD1")

    label("loc_A96")


    ChrTalk(    #41
        0xFE,
        "这次是学院事件吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "利贝尔王国到底\x01",
            "怎么回事啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD1")

    Jump("loc_EC8")

    label("loc_AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_BDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B7B")

    ChrTalk(    #43
        0xFE,
        (
            "学院放假时，让基诺奇奥\x01",
            "辅导我应考复习了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "因此对于入学考试\x01",
            "总算有点自信了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "导力器停了，\x01",
            "怪异的东西又浮在天上，\x01",
            "实在无心学习啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_BDB")

    label("loc_B7B")


    ChrTalk(    #46
        0xFE,
        (
            "多亏基诺奇奥的指导，\x01",
            "算是能应付入学考试了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "看着世间发生的事情，\x01",
            "实在没心思学习啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BDB")

    Jump("loc_EC8")

    label("loc_BDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_C9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_C33")

    ChrTalk(    #48
        0xFE,
        (
            "基诺奇奥给我当\x01",
            "家庭教师了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "好，再坚持坚持～\x01",
            "努力学习吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C99")

    label("loc_C33")

    OP_A2(0x4)

    ChrTalk(    #50
        0xFE,
        (
            "学院放假时\x01",
            "基诺奇奥给我当\x01",
            "家庭教师了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "能找到有入学考试经验的人\x01",
            "来帮忙真的是事半功倍啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C99")

    Jump("loc_EC8")

    label("loc_C9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_CA6")
    Jump("loc_EC8")

    label("loc_CA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_CE8")

    ChrTalk(    #52
        0xFE,
        "爸爸好像慌慌张张的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "……外边出什么事了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_EC8")

    label("loc_CE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_D64")

    ChrTalk(    #54
        0xFE,
        (
            "基诺奇奥\x01",
            "要是能来辅导复习\x01",
            "对我来说是再好不过的了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "但是我妈妈，却对邻居\x01",
            "有奇怪的抵触意识。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF2")

    label("loc_D64")

    OP_A2(0x4)

    ChrTalk(    #56
        0xFE,
        (
            "隔壁的基诺奇奥\x01",
            "已经是王立学院的学生了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "如果能请他来辅导我应试复习\x01",
            "我就安心多了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "但是我妈妈，却对邻居\x01",
            "有奇怪的抵触意识。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF2")

    Jump("loc_EC8")

    label("loc_DF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_EC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_E64")

    ChrTalk(    #59
        0xFE,
        (
            "但是，王立学院的入学考试\x01",
            "好像相当难的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "虽然我也很努力，\x01",
            "说实话还是很没自信啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC8")

    label("loc_E64")

    OP_A2(0x4)

    ChrTalk(    #61
        0xFE,
        (
            "我的梦想是当飞船\x01",
            "上的乘员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "到王立学院\x01",
            "学习自然科课程的话，\x01",
            "应该就能进一步接近梦想吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC8")

    TalkEnd(0xFE)
    Return()

    # Function_7_A14 end

    def Function_8_ECC(): pass

    label("Function_8_ECC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_F8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F38")

    ChrTalk(    #63
        0xFE,
        (
            "小道消息，\x01",
            "学院好像出事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "据说已经平安解决了，\x01",
            "现在王国军在学院警备哟。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_F89")

    label("loc_F38")


    ChrTalk(    #65
        0xFE,
        "学院好像出事了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "不过，据说已经平安解决了，\x01",
            "现在似乎是王国军在警备哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F89")

    Jump("loc_1341")

    label("loc_F8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1059")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1014")

    ChrTalk(    #67
        0xFE,
        (
            "唔唔，灯油\x01",
            "放在哪里了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "儿子的应试复习\x01",
            "也到了关键时刻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "无论如何要保证桌子上\x01",
            "的灯一直亮着才行啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1056")

    label("loc_1014")


    ChrTalk(    #70
        0xFE,
        (
            "唔唔，灯油\x01",
            "放在哪里了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "真是的，干脆让先生\x01",
            "去买好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1056")

    Jump("loc_1341")

    label("loc_1059")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1139")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_10C0")

    ChrTalk(    #72
        0xFE,
        (
            "家庭教师也请了，\x01",
            "这样应付考试就万全了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "好了，还有学费\x01",
            "得想办法准备好才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1136")

    label("loc_10C0")

    OP_A2(0x3)

    ChrTalk(    #74
        0xFE,
        (
            "因为王立学院放假了，\x01",
            "就拜托基诺奇奥\x01",
            "来辅导儿子的学习了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "虽然拜托邻居很不甘心，\x01",
            "为了儿子就含泪忍下来了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1136")

    Jump("loc_1341")

    label("loc_1139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1187")

    ChrTalk(    #76
        0xFE,
        (
            "儿子也相当\x01",
            "有干劲呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "上主日学校的时候\x01",
            "他自己就很用功呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1341")

    label("loc_1187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_11B6")

    ChrTalk(    #78
        0xFE,
        (
            "哎呀，什么事……\x01",
            "大街上好吵呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1341")

    label("loc_11B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1282")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_120F")

    ChrTalk(    #79
        0xFE,
        (
            "家庭教师只能\x01",
            "拜托基诺奇奥吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "拜托邻居\x01",
            "真是有点懊恼……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_127F")

    label("loc_120F")

    OP_A2(0x3)

    ChrTalk(    #81
        0xFE,
        (
            "不过儿子说了\x01",
            "一切以考试为重。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "基诺奇奥的话\x01",
            "正适合当家庭教师呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "唉，拜托邻居\x01",
            "实在有点懊恼……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_127F")

    Jump("loc_1341")

    label("loc_1282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1341")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_12EE")

    ChrTalk(    #84
        0xFE,
        (
            "不过无论如何\x01",
            "也希望儿子托尼奥\x01",
            "能考上王立学院啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "希望别有什么事\x01",
            "妨碍到他学习哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1341")

    label("loc_12EE")

    OP_A2(0x3)

    ChrTalk(    #86
        0xFE,
        (
            "真讨厌，\x01",
            "选举运动的声音这么吵……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "这样儿子学习\x01",
            "不是无法集中精神了吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1341")

    TalkEnd(0xFE)
    Return()

    # Function_8_ECC end

    def Function_9_1345(): pass

    label("Function_9_1345")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1397")

    ChrTalk(    #88
        0xFE,
        "真的出了事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "真是的，这也说那也说，\x01",
            "传言完全不能相信啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_160C")

    label("loc_1397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_147C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1427")

    ChrTalk(    #90
        0xFE,
        (
            "我预定要乘的船\x01",
            "也在海上抛锚了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "推进器的导力输出装置\x01",
            "好像完全没反应了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "没办法，我们\x01",
            "也只好在自己家待命了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1479")

    label("loc_1427")


    ChrTalk(    #93
        0xFE,
        (
            "我预定要乘的船\x01",
            "也在海上抛锚了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "推进器的导力输出装置\x01",
            "好像完全没反应了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1479")

    Jump("loc_160C")

    label("loc_147C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1548")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_14D3")

    ChrTalk(    #95
        0xFE,
        (
            "儿子好像想当\x01",
            "飞船的船员呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "嘿嘿，果然\x01",
            "是船员的儿子啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1545")

    label("loc_14D3")

    OP_A2(0x2)

    ChrTalk(    #97
        0xFE,
        (
            "儿子好像想当\x01",
            "飞船的船员呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "虽然是在天上飞的，\x01",
            "那和船也没多大区别。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "嘿嘿，果然\x01",
            "是船员的儿子啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1545")

    Jump("loc_160C")

    label("loc_1548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_160C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_158A")

    ChrTalk(    #100
        0xFE,
        (
            "诺曼先生是很出色的人，\x01",
            "但就是对公约不重视。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_160C")

    label("loc_158A")

    OP_A2(0x2)

    ChrTalk(    #101
        0xFE,
        (
            "诺曼先生是很出色的人，\x01",
            "但就是对公约不重视。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "卢安就不是旅游城市，\x01",
            "原本就是船员和渔夫的城市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "这点最好\x01",
            "别搞错了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_160C")

    TalkEnd(0xFE)
    Return()

    # Function_9_1345 end

    def Function_10_1610(): pass

    label("Function_10_1610")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_165B")

    ChrTalk(    #104
        0xFE,
        (
            "基诺奇奥哥哥\x01",
            "才不会输给考试呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "因为哥哥\x01",
            "很厉害的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1802")

    label("loc_165B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_16A6")

    ChrTalk(    #106
        0xFE,
        (
            "放假结束，\x01",
            "基诺奇奥哥哥也要回学校了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        "学校没事了吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1802")

    label("loc_16A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_16E7")

    ChrTalk(    #108
        0xFE,
        "选举的声音没有了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "叔叔们是不是\x01",
            "回家了呢～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1802")

    label("loc_16E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_171F")

    ChrTalk(    #110
        0xFE,
        "今天有主日学校。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        "啦，真期待啊⊙\x02",
    )

    CloseMessageWindow()
    Jump("loc_1802")

    label("loc_171F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1802")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1782")

    ChrTalk(    #112
        0xFE,
        (
            "基诺奇奥哥哥的学校\x01",
            "据说也很快就要放假了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "嘿嘿，等他回来\x01",
            "要尽情玩耍啊⊙\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1802")

    label("loc_1782")

    OP_A2(0x1)

    ChrTalk(    #114
        0xFE,
        (
            "嘿嘿，妈妈可是很久没有\x01",
            "一直待在家里了⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "很快基诺奇奥哥哥的\x01",
            "学校也要放假了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "果然就是要\x01",
            "大家都在家才开心啊⊙\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1802")

    TalkEnd(0xFE)
    Return()

    # Function_10_1610 end

    def Function_11_1806(): pass

    label("Function_11_1806")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_18CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1888")

    ChrTalk(    #117
        0xFE,
        "学院好像出事了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "待会儿得去\x01",
            "隔壁问问详情才行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "不管怎样现在没有消息，\x01",
            "只能靠人传言了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_18CC")

    label("loc_1888")


    ChrTalk(    #120
        0xFE,
        (
            "学院出事什么的\x01",
            "是真的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "待会儿得去\x01",
            "隔壁问问详情才行……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18CC")

    Jump("loc_1D5D")

    label("loc_18CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_19A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1951")

    ChrTalk(    #122
        0xFE,
        (
            "导力器停了，\x01",
            "日常生活也不顺心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "新市长诺曼\x01",
            "快点想想办法啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "至少桥的问题\x01",
            "得解决了才行啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_19A1")

    label("loc_1951")


    ChrTalk(    #125
        0xFE,
        (
            "导力器不能使用，\x01",
            "日常生活也不顺心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "至少桥的问题\x01",
            "得解决了才行啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19A1")

    Jump("loc_1D5D")

    label("loc_19A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1A6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A03")

    ChrTalk(    #127
        0xFE,
        (
            "儿子要当隔壁托尼奥\x01",
            "的家庭教师了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "托尼奥好像也想\x01",
            "考进王立学院的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A6B")

    label("loc_1A03")

    OP_A2(0x0)

    ChrTalk(    #129
        0xFE,
        (
            "我儿子基诺奇奥\x01",
            "要当隔壁托尼奥\x01",
            "的家庭教师了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "虽然只是放假期间，\x01",
            "但应该是不错的社会经验吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A6B")

    Jump("loc_1D5D")

    label("loc_1A6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1B44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1ACB")

    ChrTalk(    #131
        0xFE,
        (
            "一有自由的时间\x01",
            "就会考虑要做什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "忙起来明明有那么多\x01",
            "想做的事……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B41")

    label("loc_1ACB")

    OP_A2(0x0)

    ChrTalk(    #133
        0xFE,
        (
            "扫除和洗衣服都做完了，\x01",
            "女儿也去上主日学校了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "呼，难得能休息了，\x01",
            "一有自由的时间\x01",
            "真不知道该做些什么了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B41")

    Jump("loc_1D5D")

    label("loc_1B44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_1B8D")

    ChrTalk(    #135
        0xFE,
        "外面还很吵闹……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "咦，不过今天\x01",
            "不是有演讲会什么的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D5D")

    label("loc_1B8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1BE3")

    ChrTalk(    #137
        0xFE,
        (
            "女儿爱蕾塔最近\x01",
            "好像有新朋友了哟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        "这也多亏了主日学校。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C49")

    label("loc_1BE3")

    OP_A2(0x0)

    ChrTalk(    #139
        0xFE,
        (
            "女儿爱蕾塔最近\x01",
            "好像有新朋友了哟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "总是让那孩子看家\x01",
            "她一定很寂寞，\x01",
            "交了新朋友真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C49")

    Jump("loc_1D5D")

    label("loc_1C4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1D5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1CC9")

    ChrTalk(    #141
        0xFE,
        (
            "选举中游客不多，\x01",
            "向导的工作暂时停止了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "丈夫为了支援选举看起来很忙的样子，\x01",
            "不过我在家倒是很悠闲。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D5D")

    label("loc_1CC9")

    OP_A2(0x0)

    ChrTalk(    #143
        0xFE,
        (
            "我和丈夫一起\x01",
            "做旅游向导……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "选举中游客不多，\x01",
            "不过总算是暂时可以休息了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "丈夫为了支援选举看起来很忙的样子，\x01",
            "不过我在家倒是很悠闲。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D5D")

    TalkEnd(0xFE)
    Return()

    # Function_11_1806 end

    def Function_12_1D61(): pass

    label("Function_12_1D61")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1E80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E25")

    ChrTalk(    #146
        0xFE,
        (
            "儿子贝尔夫也在市长官邸\x01",
            "很努力的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "希望以这个为契机，\x01",
            "好好考虑一下将来吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "不过，还是不要着急\x01",
            "慢慢来比较重要的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "现在应该好好称赞他\x01",
            "肯工作才是。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_1E7D")

    label("loc_1E25")


    ChrTalk(    #150
        0xFE,
        (
            "儿子贝尔夫也在市长官邸\x01",
            "很努力的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "这次我们做父母的\x01",
            "可得认可那孩子才行……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E7D")

    Jump("loc_223E")

    label("loc_1E80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1F80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F1A")

    ChrTalk(    #152
        0xFE,
        (
            "我先生诺曼\x01",
            "已经好几天没从\x01",
            "市长官邸回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "身为新任市长要急迫处理事态\x01",
            "的紧张心情也能够理解……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        "只是不要太拼命了就好。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_1F7D")

    label("loc_1F1A")


    ChrTalk(    #155
        0xFE,
        (
            "我先生诺曼\x01",
            "已经好几天没从\x01",
            "市长官邸回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "唉，先生刚当上市长\x01",
            "为什么就接二连三的出事呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F7D")

    Jump("loc_223E")

    label("loc_1F80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_2055")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1FF7")

    ChrTalk(    #157
        0xFE,
        (
            "儿子贝尔夫好像去\x01",
            "老公的事务所帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "虽然不知道能持续到什么时候，\x01",
            "现在也只能先观望观望了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2052")

    label("loc_1FF7")

    OP_A2(0x7)

    ChrTalk(    #159
        0xFE,
        (
            "儿子贝尔夫好像去\x01",
            "老公的事务所帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "明明那么不愿意的……\x01",
            "为什么又去做了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2052")

    Jump("loc_223E")

    label("loc_2055")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_209F")

    ChrTalk(    #161
        0xFE,
        (
            "贝尔夫又\x01",
            "去哪里了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "好像没回仓库，\x01",
            "到底去哪儿了呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_223E")

    label("loc_209F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2169")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2109")

    ChrTalk(    #163
        0xFE,
        (
            "无论如何，那孩子\x01",
            "能回家真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "虽然可能是暂时的,\x01",
            "但待在家里就足够了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2166")

    label("loc_2109")

    OP_A2(0x7)

    ChrTalk(    #165
        0xFE,
        (
            "无论如何，那孩子\x01",
            "能回家真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "将来的事不必着急，\x01",
            "花点时间慢慢考虑就是了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2166")

    Jump("loc_223E")

    label("loc_2169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_223E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 0)), scpexpr(EXPR_END)), "loc_21D0")

    ChrTalk(    #167
        0xFE,
        (
            "老公要是能和那孩子\x01",
            "谈谈心就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "但是现在选举活动那么忙\x01",
            "连家也不能回啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_223E")

    label("loc_21D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 7)), scpexpr(EXPR_END)), "loc_21F9")

    ChrTalk(    #169
        0xFE,
        (
            "贝尔夫在２楼。\x01",
            "请上去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_223E")

    label("loc_21F9")


    ChrTalk(    #170
        0xFE,
        "真是的……那孩子……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "打算把自己关在房间里\x01",
            "到什么时候啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_223E")

    TalkEnd(0x8)
    Return()

    # Function_12_1D61 end

    def Function_13_2242(): pass

    label("Function_13_2242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 0)), scpexpr(EXPR_END)), "loc_246D")
    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_2308")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_22A9")

    ChrTalk(    #172
        0xFE,
        (
            "这种时候，不得已也得\x01",
            "去打工了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "只是，在父亲的事务所\x01",
            "工作啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2305")

    label("loc_22A9")

    OP_A2(0x6)

    ChrTalk(    #174
        0xFE,
        (
            "去北街区\x01",
            "找过工作……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "不过世间还真是残酷啊。\x01",
            "工作只有选举运动\x01",
            "的兼职什么的了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2305")

    Jump("loc_2467")

    label("loc_2308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_23F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_237B")

    ChrTalk(    #176
        0xFE,
        (
            "看来只好\x01",
            "再去找找工作了吗～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        (
            "但是，又在意伙伴们的目光，\x01",
            "港口那边的工作还是避开吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23F5")

    label("loc_237B")

    OP_A2(0x6)

    ChrTalk(    #178
        0xFE,
        (
            "就这样关在家里\x01",
            "也不是办法……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "不过伙伴们的仓库…\x01",
            "事到如今也是回不去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "唉，看来只好\x01",
            "去找找工作了吗～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23F5")

    Jump("loc_2467")

    label("loc_23F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_2467")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_242D")

    ChrTalk(    #181
        0xFE,
        "………………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_2467")

    label("loc_242D")

    OP_A2(0x6)

    ChrTalk(    #182
        0xFE,
        (
            "一直躲着\x01",
            "父亲也不是办法啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        "虽然我也明白……\x02",
    )

    CloseMessageWindow()

    label("loc_2467")

    TalkEnd(0x9)
    Jump("loc_249F")

    label("loc_246D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 7)), scpexpr(EXPR_END)), "loc_247B")
    Call(0, 17)
    Jump("loc_249F")

    label("loc_247B")

    TalkBegin(0x9)

    ChrTalk(    #184
        0xFE,
        "嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        "……唉………\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x9)

    label("loc_249F")

    Return()

    # Function_13_2242 end

    def Function_14_24A0(): pass

    label("Function_14_24A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24B1")
    Call(0, 18)

    label("loc_24B1")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_4A(0x8, 255)
    SetChrPos(0x101, -4580, 0, 62980, 360)
    SetChrPos(0xF7, -5200, 0, 62110, 360)
    SetChrPos(0x8, 2720, 0, 67920, 167)
    ClearMapFlags(0x1)
    OP_6D(-5070, 0, 64220, 0)
    OP_67(0, 8900, -10000, 0)
    OP_6B(2590, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #186
        0x101,
        (
            "#1015F#6P嗯……\x01",
            "这里是贝尔夫的家吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_259C")

    ChrTalk(    #187
        0x106,
        (
            "#051F市长官邸右侧旁\x01",
            "就是这里了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25C8")

    label("loc_259C")


    ChrTalk(    #188
        0x103,
        (
            "#020F说是市长官邸的右边，\x01",
            "应该是了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25C8")


    def lambda_25CE():
        OP_6D(210, 0, 64230, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_25CE)

    def lambda_25E6():
        OP_67(0, 8900, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_25E6)
    Sleep(1000)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    OP_8E(0x8, 0xBB8, 0x0, 0xFEB0, 0x7D0, 0x0)
    ClearChrFlags(0x8, 0x4)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x8, 256, 500)

    ChrTalk(    #189
        0x8,
        "哎呀，欢迎。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    TurnDirection(0xF7, 0x8, 500)

    def lambda_2673():
        OP_8E(0xFE, 0xFFFFFF1A, 0x0, 0xF94C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2673)
    Sleep(300)

    def lambda_2693():
        OP_6D(-1590, 0, 64160, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2693)

    def lambda_26AB():
        OP_67(0, 8900, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_26AB)
    OP_43(0x101, 0x1, 0x0, 0xF)
    Sleep(300)
    OP_43(0xF7, 0x1, 0x0, 0x10)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #190
        0x8,
        (
            "很不巧，我先生现在\x01",
            "去酒店那边了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x8,
        "能去那边找他吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        "#1004F#5P咦？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2780")

    ChrTalk(    #193
        0x106,
        (
            "#053F不，我们要找的\x01",
            "不是您先生。\x02\x03",

            "#050F而是令郎贝尔夫。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27BE")

    label("loc_2780")


    ChrTalk(    #194
        0x103,
        (
            "#026F不，我们要找的\x01",
            "不是您先生。\x02\x03",

            "#020F而是令郎\x01",
            "贝尔夫。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27BE")


    ChrTalk(    #195
        0x8,
        "哎呀哎呀，是找贝尔夫啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x8,
        (
            "抱歉哦。\x01",
            "我还以为一定是\x01",
            "为选举的事来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x101,
        (
            "#1015F#5P选举……\x02\x03",

            "#1004F啊，难不成\x01",
            "您先生是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x8,
        (
            "是的，我先生诺曼\x01",
            "参加了市长选举。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x8,
        (
            "因此，把酒店最上层\x01",
            "作为应对选举的总部使用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x8,
        (
            "各位支持者好像就是\x01",
            "在那里进行选举宣传活动的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x101,
        (
            "#1011F#5P是这样啊……\x02\x03",

            "那个，我们是\x01",
            "游击士协会的人…\x02\x03",

            "有些事，想问问\x01",
            "令郎……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x8,
        "游击士协会？\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #203
        0x8,
        (
            "那、那个，我家贝尔夫\x01",
            "做了什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_29E3")

    ChrTalk(    #204
        0x106,
        (
            "#050F不，不是那样的。\x02\x03",

            "听说令郎\x01",
            "看到了奇怪的东西。\x02\x03",

            "我们是来打听目击情报的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A42")

    label("loc_29E3")


    ChrTalk(    #205
        0x103,
        (
            "#020F不，请不必担心。\x02\x03",

            "其实听说贝尔夫\x01",
            "看到了奇怪的东西。\x02\x03",

            "我们只是来打听\x01",
            "这个目击情报的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A42")


    ChrTalk(    #206
        0x8,
        "奇怪的东西……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x101,
        (
            "#1015F#5P您\x01",
            "什么也没听说吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x8,
        "是，不好意思……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x8,
        (
            "儿子好不容易\x01",
            "回家来了，\x01",
            "却不怎么说话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x8,
        (
            "先生又为了选举拼尽全力，\x01",
            "也没和儿子好好谈谈……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x101,
        "#1025F#5P是、是这样啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2B65")

    ChrTalk(    #212
        0x106,
        (
            "#050F总之能让我们\x01",
            "和贝尔夫谈谈吗？\x02\x03",

            "如果有烦恼\x01",
            "或许能开导开导他呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BAE")

    label("loc_2B65")


    ChrTalk(    #213
        0x103,
        (
            "#020F总之，能让我们\x01",
            "和令郎谈谈吗？\x02\x03",

            "如果有烦恼\x01",
            "或许能开导开导他呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BAE")


    ChrTalk(    #214
        0x8,
        (
            "这样啊……\x01",
            "请多关照。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x8,
        (
            "贝尔夫在2楼。\x01",
            "请上去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x120F)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_14_24A0 end

    def Function_15_2BF1(): pass

    label("Function_15_2BF1")

    OP_8E(0x101, 0xFFFFEEA8, 0x0, 0xFF00, 0xBB8, 0x0)
    OP_8E(0x101, 0xFFFFF7C2, 0x0, 0xFF96, 0xBB8, 0x0)
    OP_8E(0x101, 0xFFFFF88A, 0x0, 0xF7EE, 0xBB8, 0x0)
    TurnDirection(0x101, 0x8, 500)
    Return()

    # Function_15_2BF1 end

    def Function_16_2C35(): pass

    label("Function_16_2C35")

    OP_8E(0xF7, 0xFFFFEEA8, 0x0, 0xFF00, 0xBB8, 0x0)
    OP_8E(0xF7, 0xFFFFF7C2, 0x0, 0xFF96, 0xBB8, 0x0)
    OP_8E(0xF7, 0xFFFFF916, 0x0, 0xFB22, 0xBB8, 0x0)
    TurnDirection(0xF7, 0x8, 500)
    Return()

    # Function_16_2C35 end

    def Function_17_2C79(): pass

    label("Function_17_2C79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C8A")
    Call(0, 18)

    label("loc_2C8A")

    FadeToBright(0, 0)
    EventBegin(0x0)
    OP_4A(0x9, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2D59")
    Fade(1000)
    SetChrPos(0x101, -29130, 0, 62760, 135)
    SetChrPos(0x106, -27990, 0, 62950, 180)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_0D()

    NpcTalk(    #216
        0x9,
        "年轻人",
        "嗯……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #217
        0x9,
        "年轻人",
        "……唉………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x101,
        "#1015F请问～打扰一下好吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E12")

    label("loc_2D59")

    Fade(1000)
    SetChrPos(0x101, -27990, 0, 62950, 180)
    SetChrPos(0x103, -29130, 0, 62760, 135)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_0D()

    NpcTalk(    #219
        0x9,
        "年轻人",
        "嗯……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #220
        0x9,
        "年轻人",
        "……唉………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x101,
        "#1015F#2P请问～打扰一下好吗？\x02",
    )

    CloseMessageWindow()

    label("loc_2E12")


    NpcTalk(    #222
        0x9,
        "年轻人",
        "我到底在干什么呢……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #223
        0x9,
        "年轻人",
        (
            "因为老爸不在家\x01",
            "才安心回来……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #224
        0x9,
        "年轻人",
        "……真丢脸……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3991")

    ChrTalk(    #225
        0x106,
        (
            "#551F#2P说你呢。\x02\x03",

            "我们在跟你说话呢，\x01",
            "你也回个头啊。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #226
        0x9,
        "年轻人",
        "啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x106, 400)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_2F06():
        OP_91(0x9, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2F06)
    WaitChrThread(0x9, 0x1)

    NpcTalk(    #227
        0x9,
        "年轻人",
        "呜哇哇哇！\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #228
        0x9,
        "年轻人",
        "#6P你、你们是谁！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x106,
        (
            "#050F#2P你是贝尔夫吧。\x01",
            "忘了我的脸了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x9,
        "#6P……咦…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #231
        0x9,
        "#6P啊啊，阿加特先生！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x9,
        "#6P为、为什么会在我家！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x106,
        (
            "#051F#2P有点事想问你。\x01",
            "你母亲就让我们上来了。\x02\x03",

            "现在有时间吗～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x9,
        (
            "#6P有、有……\x01",
            "倒是没什么事……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3072():
        OP_91(0x9, 0x0, 0x0, 0x15E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3072)
    WaitChrThread(0x9, 0x1)
    Sleep(500)

    ChrTalk(    #235
        0x9,
        "……那个，要问什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x101,
        (
            "#1011F其实是，听说你看见\x01",
            "『白影』了对吧。\x02\x03",

            "能不能详细\x01",
            "说说呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #237
        0x9,
        "这、这件事啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x9,
        (
            "说实话，我不太\x01",
            "想说啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x9,
        (
            "一说就会想起来的，\x01",
            "然后又被吓到……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #240
        0x106,
        "#057F#2P你说什么!\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #241
        0x9,
        (
            "我，我说！\x01",
            "说就是了嘛！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #242
        0x101,
        (
            "#1019F我说阿加特。\x01",
            "别威胁他嘛～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x106,
        (
            "#053F#2P痛快点说出来不是更好吗～？\x02\x03",

            "#050F喂，还不快说。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #244
        0x9,
        "呼……真受不了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x9,
        (
            "一周前我一直\x01",
            "都待在组织的大本营，\x01",
            "也就是那个仓库里生活的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x9,
        (
            "这个家，只是为了\x01",
            "吃饭才偶尔回来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x9,
        (
            "其他时间和伙伴们一起\x01",
            "在那里暂住。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x101,
        (
            "#1007F真、真难理解啊～\x02\x03",

            "难得这么舒服的家，\x01",
            "为什么不愿意回来呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #249
        0x101,
        (
            "#1006F阿加特以前也\x01",
            "过着一样的生活吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x106,
        (
            "#552F#2P……啰嗦。\x01",
            "别转移话题。\x02\x03",

            "#050F然后呢，怎么了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #251
        0x9,
        "一周前的夜晚……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x9,
        (
            "我和平时一样，和伙伴们\x01",
            "喝醉了睡在仓库时，\x01",
            "偶然醒来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x9,
        (
            "打算吹吹夜风来到了仓库外\x01",
            "……就看见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x101,
        (
            "#1020F看见……\x01",
            "是，是那个『白影』？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x9,
        (
            "啊啊…\x01",
            "浮在天上的『白影』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x9,
        (
            "裹着斗篷一样的\x01",
            "古老服装……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x9,
        "像跳舞一样在空中飞舞着。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #258
        0x101,
        (
            "#1016F啊、啊哈哈……\x01",
            "相当具体啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x106,
        (
            "#050F#2P既然喝醉了，\x01",
            "那喝多了眼花的可能性呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x9,
        "不，不会的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x9,
        (
            "我一下子就清醒了，\x01",
            "想叫喊但是喊不出声……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x9,
        (
            "幽灵向东北方飞走之后，\x01",
            "我才返回仓库大声把其他人\x01",
            "叫醒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x9,
        (
            "因此还被洛克\x01",
            "打了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x106,
        (
            "#053F#2P哼，原来如此。\x02\x03",

            "#050F说是晚上，\x01",
            "知道大致是几点钟吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x9,
        (
            "这个啊……\x01",
            "半夜两点左右吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x9,
        (
            "……啊啊真是的。\x01",
            "完全想起来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x9,
        (
            "明明特地跑回家\x01",
            "就是不想想起来的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x101,
        (
            "#1007F这、这就是\x01",
            "回家的理由啊。\x02\x03",

            "#1019F确实如此，不想住在看到过幽灵的地方\x01",
            "是可以理解的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x106,
        (
            "#552F#2P哼，还当什么不良少年。\x02\x03",

            "离开渡鸦帮，\x01",
            "就这样待在家里对你比较好。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #270
        0x9,
        (
            "呜呜……\x01",
            "我知道啊，我不适合当不良少年。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x9,
        (
            "但是我无论如何\x01",
            "都不想见到父亲……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x9,
        (
            "现在父亲因为选举活动\x01",
            "在宾馆暂住，\x01",
            "我才能回家……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x9,
        (
            "如果选举结束了，\x01",
            "就又要再看到他……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x9,
        (
            "如果当了市长，\x01",
            "那就会更加严格了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x101,
        (
            "#1015F嗯～说到底，\x01",
            "就是逃避自己不喜欢的事而已啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x9,
        "呜呜呜呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x106,
        (
            "#050F#2P哼，看来\x01",
            "你对自己还有所有认识的。\x02\x03",

            "#053F那就不要依靠任何人\x01",
            "自己找到答案吧。\x02\x03",

            "我们会这样\x01",
            "对你母亲说的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x9,
        "阿、阿加特先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x106,
        "#053F#2P这里的事办完了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)
    Sleep(500)

    ChrTalk(    #280
        0x106,
        "#051F#2P艾丝蒂尔，去下一站吧。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 82, 400)

    ChrTalk(    #281
        0x101,
        "#1006F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #282
        0x101,
        (
            "#1001F贝尔夫。\x01",
            "谢谢你提供情报哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x9,
        "……啊啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4691")

    label("loc_3991")

    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #284
        0x101,
        (
            "#1019F#2P真是的。\x02\x03",

            "人跟你说话呢，\x01",
            "也朝这边看看吧。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #285
        0x9,
        "年轻人",
        "啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_3A33():
        OP_91(0x9, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3A33)
    WaitChrThread(0x9, 0x1)

    NpcTalk(    #286
        0x9,
        "年轻人",
        "#6P呜哇哇哇！\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #287
        0x9,
        "年轻人",
        "#6P你、你们是谁！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x101,
        (
            "#1011F#2P终于有反应了啊。\x02\x03",

            "嗯，你就是贝尔夫？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x9,
        "#6P啊啊……是我。\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #290
        0x9,
        (
            "#6P对了，你。\x01",
            "是参加过武术大会的游击士？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x101,
        (
            "#1006F#2P艾丝蒂尔·布莱特啦。\x02\x03",

            "这位是我的前辈，\x01",
            "雪拉扎德·哈维。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x103,
        "#021F呵呵，请多关照。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x9,
        "#6P是、是……\x02",
    )

    CloseMessageWindow()

    def lambda_3B90():
        OP_91(0x9, 0x0, 0x0, 0x15E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3B90)
    WaitChrThread(0x9, 0x1)
    Sleep(500)

    ChrTalk(    #294
        0x9,
        "那到底有什么事啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x101,
        (
            "#1011F#2P其实是，听说你看见\x01",
            "『白影』了对吧。\x02\x03",

            "能不能详细\x01",
            "说说呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #296
        0x9,
        "这、这件事啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x9,
        (
            "说实话，我不太\x01",
            "想说啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x9,
        (
            "一说就会想起来的，\x01",
            "然后又被吓到……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #299
        0x101,
        (
            "#1020F#2P啊……\x02\x03",

            "那、那么恐怖的事啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x103,
        (
            "#021F好了好了。\x01",
            "别这么说啦。\x02\x03",

            "难道不能告诉\x01",
            "姐姐吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x103, 400)
    Sleep(500)

    ChrTalk(    #301
        0x9,
        "咦，但是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x103,
        (
            "#027F呵呵，只要你告诉我们\x01",
            "说不定可以给你一些好处哟㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #303
        0x9,
        "唔……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #304
        0x101,
        (
            "#1019F#2P我说雪拉姐……\x01",
            "不要诱惑他啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 82, 400)

    ChrTalk(    #305
        0x103,
        "#021F别这么死板嘛。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x9, 400)

    ChrTalk(    #306
        0x103,
        (
            "#027F那么……\x01",
            "你打算说了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #307
        0x9,
        "呼……真受不了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x9,
        (
            "一周前我一直\x01",
            "都待在组织的大本营里，\x01",
            "也就是说在那个仓库里生活着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x9,
        (
            "这个家，只是为了\x01",
            "吃饭才偶尔回来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x9,
        (
            "其他时间和伙伴们一起\x01",
            "在那里暂住。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x101,
        (
            "#1007F#2P真、真难理解啊～\x02\x03",

            "难得这么舒服的家，\x01",
            "为什么不愿意回来呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x103,
        (
            "#021F呵呵。\x01",
            "年轻人就是这样吧。\x02\x03",

            "#027F那么，之后呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x9,
        "一周前的夜晚……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x9,
        (
            "我和平时一样，和伙伴们\x01",
            "喝醉了在仓库里睡觉时，\x01",
            "偶然醒来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x9,
        (
            "打算到仓库外吹吹夜风的，\x01",
            "……就看见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x101,
        (
            "#1020F#2P看见……\x01",
            "是，是那个『白影』？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x9,
        (
            "啊啊…\x01",
            "浮在天上的『白影』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x9,
        (
            "裹着斗篷一样的\x01",
            "古老服装……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x9,
        "像跳舞一样在空中飞舞着。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #320
        0x101,
        (
            "#1016F#2P啊、啊哈哈……\x01",
            "相当具体啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x103,
        (
            "#020F既然喝醉了，\x01",
            "那喝多了眼花的可能性呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x9,
        "不，不会的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x9,
        (
            "我一下子就清醒了，\x01",
            "想叫喊但是喊不出声……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x9,
        (
            "幽灵向东北方飞走之后，\x01",
            "我才返回仓库大声把其他人\x01",
            "叫醒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0x9,
        (
            "因此还被洛克\x01",
            "打了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x103,
        (
            "#026F唔，原来如此啊。\x02\x03",

            "#020F说是晚上，\x01",
            "知道具体是几点钟吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x9,
        (
            "是啊……\x01",
            "半夜两点左右吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x9,
        (
            "……啊啊真是的。\x01",
            "完全想起来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x9,
        (
            "明明特地跑回家\x01",
            "就是不想想起来的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x101,
        (
            "#1007F#2P这、这就是\x01",
            "回家的理由啊。\x02\x03",

            "#1019F确实如此，不想住在看到过幽灵的地方，\x01",
            "这是可以理解的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x103,
        (
            "#027F呵呵，这不是深切地\x01",
            "感受到家的温暖了嘛。\x02\x03",

            "以此为机会，别再当什么\x01",
            "不良少年不就好了？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #332
        0x9,
        (
            "呜呜……\x01",
            "我知道啊，我不适合当不良少年。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x9,
        (
            "但是我无论如何\x01",
            "都不想见到父亲……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0x9,
        (
            "现在父亲因为选举活动\x01",
            "在酒店暂住\x01",
            "我才能回家……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x9,
        (
            "如果选举结束了，\x01",
            "就又要再看到他……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x9,
        (
            "如果当了市长\x01",
            "那就会更加严格了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x101,
        (
            "#1015F#2P嗯～说到底，\x01",
            "就是逃避自己不喜欢的事而已啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x9,
        "呜呜呜呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x103,
        "#021F好了好了，打起精神来。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x103, 0x40)
    OP_8F(0x103, 0xFFFF90FC, 0x0, 0xF0FA, 0x3E8, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #340
        (
            "\x07\x05雪拉扎德\x01",
            "在贝尔夫脸颊上吻了一下。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #341
        0x9,
        "呜哇啊！\x02",
    )

    OP_96(0x9, 0xFFFF9304, 0x0, 0xEEB6, 0x1F4, 0x1388)
    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8F(0x103, 0xFFFF8F30, 0x0, 0xF42E, 0x4B0, 0x0)
    ClearChrFlags(0x103, 0x40)
    TurnDirection(0x9, 0x103, 800)
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(    #342
        0x101,
        "#1013F#2P我、我说雪拉姐！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x103,
        (
            "#021F呵呵，这是提供情报的\x01",
            "感谢兼鼓励哟。\x02\x03",

            "#027F之后你自己思考\x01",
            "找出答案就好。\x02\x03",

            "你的事只有你自己\x01",
            "才能找到答案。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0x9,
        "姐，姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0x103,
        (
            "#026F那么……\x01",
            "这里就这样吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 82, 400)
    Sleep(500)

    ChrTalk(    #346
        0x103,
        "#020F艾丝蒂尔，去下一站吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x101,
        "#1007F#2P唉……真服了雪拉姐。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)
    Sleep(500)

    ChrTalk(    #348
        0x101,
        (
            "#1008F#2P贝尔夫。\x01",
            "谢谢你提供情报哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #349
        0x9,
        "噢！\x02",
    )

    CloseMessageWindow()

    label("loc_4691")

    OP_A2(0x1210)
    OP_28(0x82, 0x2, 0x20)
    OP_28(0x82, 0x1, 0x40)
    OP_4B(0x9, 255)
    ClearChrFlags(0x9, 0x10)
    EventEnd(0x0)
    Return()

    # Function_17_2C79 end

    def Function_18_46AC(): pass

    label("Function_18_46AC")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4726"),
        (1, "loc_472C"),
        (SWITCH_DEFAULT, "loc_4732"),
    )


    label("loc_4726")

    OP_A2(0x1200)
    Jump("loc_4732")

    label("loc_472C")

    OP_A2(0x1201)
    Jump("loc_4732")

    label("loc_4732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4740")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_4744")

    label("loc_4740")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_4744")

    Return()

    # Function_18_46AC end

    SaveToFile()

Try(main)
