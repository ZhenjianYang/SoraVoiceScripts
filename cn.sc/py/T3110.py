from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3110   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        '露依赛',                               # 9
        '乌缇',                                 # 10
        '鲁特尔',                               # 11
        '索黛丽娅',                             # 12
        '斯坦因',                               # 13
        '阿利瑟',                               # 14
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
        'ED6_DT07/CH01430 ._CH',             # 00
        'ED6_DT07/CH01070 ._CH',             # 01
        'ED6_DT07/CH01020 ._CH',             # 02
        'ED6_DT07/CH01030 ._CH',             # 03
        'ED6_DT07/CH01200 ._CH',             # 04
        'ED6_DT07/CH01130 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01430P._CP',             # 00
        'ED6_DT07/CH01070P._CP',             # 01
        'ED6_DT07/CH01020P._CP',             # 02
        'ED6_DT07/CH01030P._CP',             # 03
        'ED6_DT07/CH01200P._CP',             # 04
        'ED6_DT07/CH01130P._CP',             # 05
    )

    DeclNpc(
        X                   = -190,
        Z                   = 0,
        Y                   = 23730,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -1840,
        Z                   = 4000,
        Y                   = 23380,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 24940,
        Z                   = 0,
        Y                   = 530,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -4040,
        Z                   = 0,
        Y                   = 3790,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 48200,
        Z                   = 0,
        Y                   = 23060,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 27890,
        Z                   = 0,
        Y                   = 22500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )


    ScpFunction(
        "Function_0_19A",          # 00, 0
        "Function_1_219",          # 01, 1
        "Function_2_21A",          # 02, 2
        "Function_3_397",          # 03, 3
        "Function_4_3BB",          # 04, 4
        "Function_5_3DF",          # 05, 5
        "Function_6_4B0",          # 06, 6
        "Function_7_D66",          # 07, 7
        "Function_8_1008",         # 08, 8
        "Function_9_16D0",         # 09, 9
        "Function_10_1B26",        # 0A, 10
    )


    def Function_0_19A(): pass

    label("Function_0_19A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1B3")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_218")

    label("loc_1B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1C2")
    SetChrFlags(0xA, 0x80)
    Jump("loc_218")

    label("loc_1C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1DD")
    SetChrPos(0x9, 940, 0, 23830, 319)
    Jump("loc_218")

    label("loc_1DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_1F8")
    SetChrPos(0x9, 940, 0, 23830, 319)
    Jump("loc_218")

    label("loc_1F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_202")
    Jump("loc_218")

    label("loc_202")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_218")
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x10)

    label("loc_218")

    Return()

    # Function_0_19A end

    def Function_1_219(): pass

    label("Function_1_219")

    Return()

    # Function_1_219 end

    def Function_2_21A(): pass

    label("Function_2_21A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23F")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_381")

    label("loc_23F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_258")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_381")

    label("loc_258")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_271")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_381")

    label("loc_271")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28A")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_381")

    label("loc_28A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A3")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_381")

    label("loc_2A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BC")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_381")

    label("loc_2BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D5")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_381")

    label("loc_2D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EE")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_381")

    label("loc_2EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_307")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_381")

    label("loc_307")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_320")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_381")

    label("loc_320")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_339")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_381")

    label("loc_339")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_352")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_381")

    label("loc_352")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36B")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_381")

    label("loc_36B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_381")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_381")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_396")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_381")

    label("loc_396")

    Return()

    # Function_2_21A end

    def Function_3_397(): pass

    label("Function_3_397")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3BA")
    OP_8D(0xFE, 25620, 1830, 23470, -690, 1000)
    Jump("Function_3_397")

    label("loc_3BA")

    Return()

    # Function_3_397 end

    def Function_4_3BB(): pass

    label("Function_4_3BB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3DE")
    OP_8D(0xFE, 48200, 23060, 51000, 22330, 1000)
    Jump("Function_4_3BB")

    label("loc_3DE")

    Return()

    # Function_4_3BB end

    def Function_5_3DF(): pass

    label("Function_5_3DF")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_4AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_453")

    ChrTalk(    #0
        0xFE,
        (
            "如果是那种程度的摇晃，\x01",
            "中央工房应该还不要紧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "啊啊～晚了晚了～\x01",
            "再不赶快出勤可不行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AC")

    label("loc_453")


    ChrTalk(    #2
        0xFE,
        (
            "呀～地震\x01",
            "真是很久没遇到过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "一开始我还以为是拉赛尔博士\x01",
            "又在搞什么试验了，\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_4AC")

    TalkEnd(0x8)
    Return()

    # Function_5_3DF end

    def Function_6_4B0(): pass

    label("Function_6_4B0")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_5C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55A")

    ChrTalk(    #4
        0xFE,
        (
            "导力器不能用了，\x01",
            "大家都很困扰…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "但我和姐姐\x01",
            "却一点也不在乎。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "因为我们基本上\x01",
            "都不会使用厨房。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "倒是姐姐的男朋友\x01",
            "乌尔斯偶尔会用，\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_5C3")

    label("loc_55A")


    ChrTalk(    #8
        0xFE,
        (
            "乌尔斯再过一会\x01",
            "应该就会过来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "姐姐忙的时候他总是\x01",
            "会把午餐送来，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "而且还会帮忙\x01",
            "做扫除呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C3")

    Jump("loc_D62")

    label("loc_5C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_8BB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_798")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x417, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_714")
    OP_62(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(    #11
        0xFE,
        (
            "啊～提妲，\x01",
            "真是好久不见了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "难道你们\x01",
            "今天也在帮博士的忙吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x107,
        (
            "#560F啊，嗯～\x01",
            "是呀。\x02\x03",

            "乌缇你\x01",
            "又在看家吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "嗯～是呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "露依赛姐姐总是\x01",
            "对什么事都充满兴趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "能乘坐上『埃尔赛尤』\x01",
            "她好像特别兴奋呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "真是像个小孩子一样……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x107,
        "#067F啊、啊哈哈……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20BB)
    Jump("loc_795")

    label("loc_714")


    ChrTalk(    #19
        0xFE,
        (
            "我姐姐虽然头脑聪明，\x01",
            "但完全是小孩子脾气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "就算把房间收拾好了，\x01",
            "马上又会恢复原样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "倒是提妲给人的感觉\x01",
            "像个大人呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_795")

    Jump("loc_8B8")

    label("loc_798")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_845")

    ChrTalk(    #22
        0xFE,
        (
            "露依赛姐姐最近\x01",
            "好像非常兴奋呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "能乘坐上『埃尔赛尤』\x01",
            "她好像特别兴奋呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "今天也说要研究什么异变，\x01",
            "一大早就离开家了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        "真是像个小孩子一样……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_8B8")

    label("loc_845")


    ChrTalk(    #26
        0xFE,
        (
            "姐姐虽然头脑聪明，\x01",
            "但其实完全是小孩子脾气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "比起探明异变的原因，\x01",
            "我倒是更想知道为什么\x01",
            "家里总是一团乱糟。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B8")

    Jump("loc_D62")

    label("loc_8BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_9A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_918")

    ChrTalk(    #28
        0xFE,
        (
            "啊啊～～真希望我姐姐\x01",
            "早点嫁出去啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "不然房间永远都\x01",
            "不能恢复整洁。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A4")

    label("loc_918")


    ChrTalk(    #30
        0xFE,
        (
            "我姐姐因为工作上的事情\x01",
            "到要塞去了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "也就是说，如果现在把房间收拾好，\x01",
            "就可以保持干净一阵子了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "嗯，有干劲了，\x01",
            "加油做扫除！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_9A4")

    Jump("loc_D62")

    label("loc_9A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_B35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A19")
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(    #33
        0xFE,
        (
            "帮博士的忙…\x01",
            "真的好厉害啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "如果是我姐姐的话就肯定不行～\x01",
            "我可以１２０％的确定。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B32")

    label("loc_A19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x286, 3)), scpexpr(EXPR_END)), "loc_A7D")

    ChrTalk(    #35
        0xFE,
        (
            "姐姐因为工作上的事情\x01",
            "到要塞那边去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "呼，真希望她能在出发前\x01",
            "把房间收拾一下啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B32")

    label("loc_A7D")

    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(    #37
        0xFE,
        (
            "啊～提妲。\x01",
            "今天也在帮博士的忙吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x107,
        (
            "#060F啊，嗯～是呀。\x02\x03",

            "我们要去设置\x01",
            "最新开发的观测装置。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "是吗～其实也只能如此呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "可以帮到博士的人\x01",
            "大概只有提妲了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_A2(0x1433)

    label("loc_B32")

    Jump("loc_D62")

    label("loc_B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_C5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x286, 3)), scpexpr(EXPR_END)), "loc_BA7")
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(    #41
        0xFE,
        (
            "帮博士的忙…\x01",
            "真的好厉害啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "如果是我姐姐的话就肯定不行～\x01",
            "我可以１２０％的确定。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C59")

    label("loc_BA7")

    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(    #43
        0xFE,
        (
            "啊～提妲。\x01",
            "今天也在帮博士的忙吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x107,
        (
            "#060F啊，嗯～是呀。\x02\x03",

            "我们要去设置\x01",
            "最新开发的观测装置。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "是吗～其实也只能如此呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "可以帮到博士的人\x01",
            "大概只有提妲了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1433)

    label("loc_C59")

    Jump("loc_D62")

    label("loc_C5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_CB6")

    ChrTalk(    #47
        0xFE,
        (
            "在露依赛姐姐回来之前\x01",
            "书就这样扔着就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "这次一定要让她\x01",
            "自己整理。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D62")

    label("loc_CB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_D62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_D19")

    ChrTalk(    #49
        0xFE,
        (
            "真是的～姐姐从来都\x01",
            "不会整理房间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "她的男朋友乌尔斯先生\x01",
            "为此也很辛苦呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D62")

    label("loc_D19")


    ChrTalk(    #51
        0xFE,
        (
            "真讨厌～刚才的地震\x01",
            "把书震落了一地～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "姐姐又不把它们\x01",
            "收拾好～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_D62")

    TalkEnd(0x9)
    Return()

    # Function_6_4B0 end

    def Function_7_D66(): pass

    label("Function_7_D66")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_E56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_DE6")

    ChrTalk(    #53
        0xFE,
        (
            "不久后又要去王都\x01",
            "和共和国的人商谈了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "如果输出工作这样发展下去的话，\x01",
            "飞船产业的未来倒是很光明呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E53")

    label("loc_DE6")


    ChrTalk(    #55
        0xFE,
        (
            "最近利用飞船的\x01",
            "合作越来越多，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "是发展商业渠道的好机会。\x01",
            "我也高兴得很啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "高兴得都想大喊了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_E53")

    Jump("loc_1004")

    label("loc_E56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_F13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_EBB")

    ChrTalk(    #58
        0xFE,
        (
            "等工作告一段落之后\x01",
            "我准备去中央工房拜访。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "那孩子一定\x01",
            "给大家添了不少麻烦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F10")

    label("loc_EBB")


    ChrTalk(    #60
        0xFE,
        (
            "我的女儿进入中央工房\x01",
            "工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "虽然她的动机不正…\x01",
            "但还是希望她能加油干。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_F10")

    Jump("loc_1004")

    label("loc_F13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_1004")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_F6E")

    ChrTalk(    #62
        0xFE,
        (
            "刚才我也忍不住\x01",
            "大声惊叫了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "身为飞船商人，\x01",
            "真是有些不好意思啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1004")

    label("loc_F6E")


    ChrTalk(    #64
        0xFE,
        (
            "啊～在飞船坪的时候\x01",
            "真是吓了一跳呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "虽然脑子里明白不会有什么危险，\x01",
            "但还是不由自主地大叫了起来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "身为飞船商人，\x01",
            "真是有些不好意思啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1004")

    TalkEnd(0xA)
    Return()

    # Function_7_D66 end

    def Function_8_1008(): pass

    label("Function_8_1008")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_10F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10A3")

    ChrTalk(    #67
        0xFE,
        (
            "为了重新展开研究工作，\x01",
            "中央工房好像非常忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "去做事务见习工作，\x01",
            "对我女儿米优也有好处。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "那个孩子没有\x01",
            "什么工作经验，\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_10F5")

    label("loc_10A3")


    ChrTalk(    #70
        0xFE,
        (
            "为了重新展开研究工作，\x01",
            "中央工房好像非常忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "能长点见识\x01",
            "对她也有好处。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10F5")

    Jump("loc_16CC")

    label("loc_10F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_121D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A8")

    ChrTalk(    #72
        0xFE,
        (
            "导力器瘫痪之后，\x01",
            "城里发生了很大的骚乱呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "一群人都围到了中央工房，\x01",
            "工房长也被吓得很惨。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "这次的情况和上一次很像，\x01",
            "大概又是同一伙犯人做的吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_121A")

    label("loc_11A8")


    ChrTalk(    #75
        0xFE,
        (
            "虽然搞破坏的那些家伙难逃其罪，\x01",
            "但我们自己其实也有责任。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "做实验引起不良异变的事情\x01",
            "也有过不止一次两次了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_121A")

    Jump("loc_16CC")

    label("loc_121D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_132E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1286")

    ChrTalk(    #77
        0xFE,
        (
            "呼～今天总算把\x01",
            "丈夫和女儿平安送走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "这样在爷爷回来之前\x01",
            "可以好好休息一下了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_132B")

    label("loc_1286")


    ChrTalk(    #79
        0xFE,
        (
            "呼～今天总算把\x01",
            "丈夫和女儿平安送走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "这样在爷爷回来之前\x01",
            "可以好好休息一下了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "我家的爷爷在白天\x01",
            "总是泡在酒馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "但他却并不喝酒，\x01",
            "真是个怪人呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_132B")

    Jump("loc_16CC")

    label("loc_132E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1415")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1397")

    ChrTalk(    #83
        0xFE,
        (
            "听我老公说，最近和帝国那边\x01",
            "的商谈好像增多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "难道是和帝国的关系\x01",
            "有了好转吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1412")

    label("loc_1397")


    ChrTalk(    #85
        0xFE,
        (
            "我老公的职业是飞船交易\x01",
            "的中介商人，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "最近不知为什么总是出差。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "不久前才刚从柏斯回来，\x01",
            "这次马上又要去王都。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1412")

    Jump("loc_16CC")

    label("loc_1415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_1531")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1478")

    ChrTalk(    #88
        0xFE,
        (
            "那个孩子能认真工作\x01",
            "真是让我意外。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "也许是隐藏的工作欲望\x01",
            "终于被激发了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_152E")

    label("loc_1478")

    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(    #90
        0xFE,
        "啊～提妲。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "我女儿有没有\x01",
            "认真工作呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x107,
        (
            "#560F啊～米优一直\x01",
            "很努力工作呢。\x02\x03",

            "总是东奔西走忙个不停。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        "嘿～？那可真是有点意外啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "我还以为她会\x01",
            "经常偷懒呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_152E")

    Jump("loc_16CC")

    label("loc_1531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1607")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1594")

    ChrTalk(    #95
        0xFE,
        (
            "我女儿米优\x01",
            "去中央工房帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "动机暂且不说，总之\x01",
            "对工作有兴趣就是好事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1604")

    label("loc_1594")


    ChrTalk(    #97
        0xFE,
        (
            "我女儿米优\x01",
            "去中央工房帮忙了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "她似乎本想当\x01",
            "接待处的小姐的…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "算了，也是个接触社会\x01",
            "的好机会…\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1604")

    Jump("loc_16CC")

    label("loc_1607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_16CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1665")

    ChrTalk(    #100
        0xFE,
        "话说回来，地震真是好久没遇到了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "已经都快把那种东西\x01",
            "给忘掉了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16CC")

    label("loc_1665")


    ChrTalk(    #102
        0xFE,
        "我很讨厌地震呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "脚下摇晃个不停，\x01",
            "真是让人不舒服。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "嗯，而且连飞船\x01",
            "也都无法乘坐了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_16CC")

    TalkEnd(0xB)
    Return()

    # Function_8_1008 end

    def Function_9_16D0(): pass

    label("Function_9_16D0")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_17E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1738")

    ChrTalk(    #105
        0xFE,
        (
            "地震倒是无所谓，\x01",
            "还是互不侵犯条约比较重要。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "毕竟是关系到王国未来\x01",
            "的问题。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17E0")

    label("loc_1738")


    ChrTalk(    #107
        0xFE,
        (
            "嗯，再过不久就是\x01",
            "互不侵犯条约的签字仪式了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "那次的战争已经过去十年了…\x01",
            "也是该和帝国清算一下历史问题的时候了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "如果能顺利签署条约\x01",
            "自然是最好不过了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_17E0")

    Jump("loc_1B22")

    label("loc_17E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1903")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_185A")

    ChrTalk(    #110
        0xFE,
        (
            "店长耶鲁克\x01",
            "购进了新型枪……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        "你们可以去看看。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "如果能找到优秀的射手\x01",
            "帮忙测试一下就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1900")

    label("loc_185A")


    ChrTalk(    #113
        0xFE,
        (
            "前几天中央工房的加鲁诺\x01",
            "给我看了新型的导力枪呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "虽然细微部分还有点粗糙，\x01",
            "但驱动部分却有着革命性的改进。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "如果好好测试一下，\x01",
            "以后很可能会成为热销品。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1900")

    Jump("loc_1B22")

    label("loc_1903")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1A4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_19B5")

    ChrTalk(    #116
        0xFE,
        (
            "我经营的武器店一向\x01",
            "不贩卖最新型的武器产品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "以前我们一直遵循这个方针，\x01",
            "也遭到了很多年轻人的不解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "不过，他们现在也理解了，\x01",
            "并且也认同了我的想法。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A49")

    label("loc_19B5")


    ChrTalk(    #119
        0xFE,
        (
            "我经营的武器店一向\x01",
            "不贩卖最新型的武器产品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "新型的武器，其性能\x01",
            "再怎么说也不是很稳定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "只有经过一段时间的测试\x01",
            "才能明白其中的缺陷。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1A49")

    Jump("loc_1B22")

    label("loc_1A4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_1B22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1AB5")

    ChrTalk(    #122
        0xFE,
        (
            "我在蔡斯市内\x01",
            "经营武器店，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "就是游击士协会对面的那家店，\x01",
            "有机会的话多来光顾吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B22")

    label("loc_1AB5")


    ChrTalk(    #124
        0xFE,
        (
            "嗯，好像没有余震了，\x01",
            "店应该不要紧吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "不过真奇怪，竟然会有地震。\x01",
            "利贝尔可是很少发生地震的啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1B22")

    TalkEnd(0xC)
    Return()

    # Function_9_16D0 end

    def Function_10_1B26(): pass

    label("Function_10_1B26")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1C26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC5")

    ChrTalk(    #126
        0xFE,
        (
            "导力器不能用了，\x01",
            "我就买来了固形燃料。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "『贝尔杂货店』\x01",
            "卖的东西真是齐全啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "有这么商品齐全的店在附近，\x01",
            "实在是让人很安心。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1C23")

    label("loc_1BC5")


    ChrTalk(    #129
        0xFE,
        (
            "导力器不能用了，\x01",
            "我就买来了固形燃料。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "虽然火力有些弱，\x01",
            "但也可以好好练习一下烹饪了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C23")

    Jump("loc_1CA2")

    label("loc_1C26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1CA2")

    ChrTalk(    #131
        0xFE,
        (
            "老公带着温丝\x01",
            "去中央工房了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "说是要去顶楼\x01",
            "观察传闻中的浮游物体…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "那么可怕的东西\x01",
            "确实让人无法不在意吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CA2")

    TalkEnd(0xFE)
    Return()

    # Function_10_1B26 end

    SaveToFile()

Try(main)
