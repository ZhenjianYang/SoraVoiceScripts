from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0111   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0111.x',
        MapIndex            = 11,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0111_1 ._SN',
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
        '拉欧老人',                             # 9
        '亚尔丽 ',                              # 10
        '胡里奥',                               # 11
        '菲特 ',                                # 12
        '尤妮',                                 # 13
        '芙莉莎',                               # 14
        '阿妮娅',                               # 15
        '加通老大',                             # 16
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
        'ED6_DT07/CH01000 ._CH',             # 00
        'ED6_DT07/CH01030 ._CH',             # 01
        'ED6_DT07/CH01040 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01170 ._CH',             # 04
        'ED6_DT07/CH01130 ._CH',             # 05
        'ED6_DT07/CH01070 ._CH',             # 06
        'ED6_DT07/CH01530 ._CH',             # 07
        'ED6_DT26/CH20330 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH01000P._CP',             # 00
        'ED6_DT07/CH01030P._CP',             # 01
        'ED6_DT07/CH01040P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01170P._CP',             # 04
        'ED6_DT07/CH01130P._CP',             # 05
        'ED6_DT07/CH01070P._CP',             # 06
        'ED6_DT07/CH01530P._CP',             # 07
        'ED6_DT26/CH20330P._CP',             # 08
    )

    DeclNpc(
        X                   = -35400,
        Z                   = 0,
        Y                   = 36030,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -39940,
        Z                   = 0,
        Y                   = 33130,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -42500,
        Z                   = 0,
        Y                   = 37200,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 37070,
        Z                   = 0,
        Y                   = 33560,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 38800,
        Z                   = 0,
        Y                   = 30060,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -4550,
        Z                   = 0,
        Y                   = 37480,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 3140,
        Z                   = 0,
        Y                   = 32100,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 4600,
        Z                   = 0,
        Y                   = 31530,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )


    ScpFunction(
        "Function_0_1F2",          # 00, 0
        "Function_1_326",          # 01, 1
        "Function_2_35D",          # 02, 2
        "Function_3_4DA",          # 03, 3
        "Function_4_4FE",          # 04, 4
        "Function_5_10C7",         # 05, 5
        "Function_6_1553",         # 06, 6
        "Function_7_1922",         # 07, 7
        "Function_8_1AA4",         # 08, 8
        "Function_9_20D8",         # 09, 9
        "Function_10_253E",        # 0A, 10
        "Function_11_2C2E",        # 0B, 11
        "Function_12_302F",        # 0C, 12
    )


    def Function_0_1F2(): pass

    label("Function_0_1F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_24D")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x8, -39720, 0, 35090, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A")
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xD, 5460, 0, 34000, 90)
    SetChrPos(0xE, 2390, 0, 31560, 51)
    OP_43(0xE, 0x0, 0x0, 0x2)

    label("loc_24A")

    Jump("loc_306")

    label("loc_24D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_28C")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xC, 37990, 0, 33540, 315)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_279")
    SetChrFlags(0xF, 0x80)

    label("loc_279")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_289")
    SetChrFlags(0xF, 0x10)

    label("loc_289")

    Jump("loc_306")

    label("loc_28C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_2BA")
    SetChrPos(0x8, -41180, 0, 38000, 270)
    OP_4A(0x8, 255)
    SetChrChipByIndex(0x8, 8)
    SetChrSubChip(0x8, 7)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_306")

    label("loc_2BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_2F2")
    SetChrFlags(0xC, 0x10)
    SetChrPos(0x8, -41180, 0, 38000, 270)
    OP_4A(0x8, 255)
    SetChrChipByIndex(0x8, 8)
    SetChrSubChip(0x8, 7)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_306")

    label("loc_2F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_306")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_306")

    label("loc_306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_317")
    OP_A3(0x10F0)
    Event(0, 12)
    Jump("loc_325")

    label("loc_317")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_325")
    OP_A3(0x10F1)
    Event(1, 3)

    label("loc_325")

    Return()

    # Function_0_1F2 end

    def Function_1_326(): pass

    label("Function_1_326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_330")
    Jump("loc_35C")

    label("loc_330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_341")
    OP_6F(0x2, 15)
    Jump("loc_35C")

    label("loc_341")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_352")
    OP_6F(0x2, 15)
    Jump("loc_35C")

    label("loc_352")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_35C")
    Jump("loc_35C")

    label("loc_35C")

    Return()

    # Function_1_326 end

    def Function_2_35D(): pass

    label("Function_2_35D")

    RunExpression(0xE, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_382")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_4C4")

    label("loc_382")

    Jc((scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39B")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_4C4")

    label("loc_39B")

    Jc((scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B4")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_4C4")

    label("loc_3B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CD")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_4C4")

    label("loc_3CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E6")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_4C4")

    label("loc_3E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FF")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_4C4")

    label("loc_3FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_418")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_4C4")

    label("loc_418")

    Jc((scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_431")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_4C4")

    label("loc_431")

    Jc((scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44A")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_4C4")

    label("loc_44A")

    Jc((scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_463")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_4C4")

    label("loc_463")

    Jc((scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47C")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_4C4")

    label("loc_47C")

    Jc((scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_495")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_4C4")

    label("loc_495")

    Jc((scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AE")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_4C4")

    label("loc_4AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C4")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_4C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4D9")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_4C4")

    label("loc_4D9")

    Return()

    # Function_2_35D end

    def Function_3_4DA(): pass

    label("Function_3_4DA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4FD")
    OP_8D(0xFE, -447, 33095, 4354, 30386, 4000)
    Jump("Function_3_4DA")

    label("loc_4FD")

    Return()

    # Function_3_4DA end

    def Function_4_4FE(): pass

    label("Function_4_4FE")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_87E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x413, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71B")
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x102, 0)
    Sleep(1000)

    ChrTalk(    #0
        0xFE,
        (
            "哟，艾丝蒂尔啊……\x01",
            "这，这不是约修亚吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        "#1035F好久不见了，菲特先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "哟，才多久没见啊，\x01",
            "就完全长成个男子汉了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "嗯，这我就放心了。\x01",
            "和艾丝蒂尔在游击士的道路上都\x01",
            "做得很漂亮嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x102,
        "#1040F这都是托您的福。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "看来王国中\x01",
            "好像发生了严重的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "回归军队的卡西乌斯\x01",
            "也忙得不可开交吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #7
        0xFE,
        (
            "作为游击士的你们两个\x01",
            "可要努力，不能输给他哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1006F嗯！\x01",
            "我们会尽全力完成工作的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        (
            "#1040F有什么困难\x01",
            "就联系协会吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #10
        0xFE,
        (
            "我会的。\x01",
            "那么，两人都要小心。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x209B)
    Jump("loc_87B")

    label("loc_71B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_761")

    ChrTalk(    #11
        0xFE,
        (
            "有什么事我\x01",
            "会联络协会的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "那么，两人都要小心。\x02",
    )

    CloseMessageWindow()
    OP_A3(0x1)
    Jump("loc_87B")

    label("loc_761")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_823")

    ChrTalk(    #13
        0xFE,
        (
            "这么说来，礼拜堂\x01",
            "好像在举行婚礼……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "虽然是大喜的日子，\x01",
            "却碰上事件实在是不走运。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "我也是有女儿的父亲，\x01",
            "理解父母的难处。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "唉，希望尤妮\x01",
            "结婚的时候别发生什么事就好。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_87B")

    label("loc_823")


    ChrTalk(    #17
        0xFE,
        (
            "虽然是大喜的日子\x01",
            "碰上这样的事件……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "唉，希望尤妮\x01",
            "结婚的时候别发生什么事就好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87B")

    Jump("loc_10C3")

    label("loc_87E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_948")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8D4")

    ChrTalk(    #19
        0xFE,
        "怎么能让尤妮离开我。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "真让人感动……\x01",
            "天下父母心都是相通的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_945")

    label("loc_8D4")


    ChrTalk(    #21
        0xFE,
        (
            "虽说可以出去了，\x01",
            "还是不能让尤妮离开我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "……亲子深情\x01",
            "到任何地方都是一样的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "真是……太感人了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_945")

    Jump("loc_10C3")

    label("loc_948")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_A36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9B9")

    ChrTalk(    #24
        0xFE,
        (
            "虽说阿斯顿的部队来了，\x01",
            "但雾没散之前都不能疏忽大意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "总之不能让女儿尤妮\x01",
            "离开我的视线。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A33")

    label("loc_9B9")


    ChrTalk(    #26
        0xFE,
        (
            "看来阿斯顿的部队\x01",
            "已经开始城市警备了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "可是，雾没散之前\x01",
            "还是不能安心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "总之不能让女儿尤妮\x01",
            "离开我的视线。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_A33")

    Jump("loc_10C3")

    label("loc_A36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_B55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AAB")

    ChrTalk(    #29
        0xFE,
        (
            "尤妮也一直\x01",
            "不敢看我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "虽说是为了保护女儿，\x01",
            "发火也不像是平常的我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "真让人沮丧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_B52")

    label("loc_AAB")


    ChrTalk(    #32
        0xFE,
        (
            "今天早上，尤妮\x01",
            "不听话想要跑出门。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "我发现的时候\x01",
            "就大声骂了她几句。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "虽说是为了女儿的安全，\x01",
            "但如此失态真是太不像我了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "不知道会不会\x01",
            "被尤妮讨厌……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_B52")

    Jump("loc_10C3")

    label("loc_B55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_EFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x312, 0)), scpexpr(EXPR_END)), "loc_D12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BC8")

    ChrTalk(    #36
        0xFE,
        "差不多到了互不侵犯条约的签字议式了吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "说得乐观点，\x01",
            "这个国家前途光明啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7B")

    label("loc_BC8")


    ChrTalk(    #38
        0xFE,
        (
            "说起来，差不多是\x01",
            "互不侵犯条约的签字议式了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "卡西乌斯一定也为了警备什么的\x01",
            "忙得不可开交吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "不过，因为这是对王国的将来\x01",
            "举足轻重的条约啊。\x01",
            "希望能平安签订下来啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_C7B")

    Jump("loc_D0F")

    label("loc_C7E")


    ChrTalk(    #41
        0xFE,
        (
            "洛连特支部由于人手不足，\x01",
            "这阵子真是快忙翻了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "不但少了卡西乌斯，\x01",
            "雪拉扎德也经常不在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "这次两人一起回来了，\x01",
            "就麻烦你们补这个空啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D0F")

    Jump("loc_EF8")

    label("loc_D12")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #44
        0xFE,
        (
            "哦，这不是艾丝蒂尔\x01",
            "和雪拉扎德吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "好久不见啦。\x01",
            "还好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#1016F嗯，很好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x103,
        "#020F事情很多，一直忙得很呢。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 4)), scpexpr(EXPR_END)), "loc_E09")

    ChrTalk(    #48
        0xFE,
        (
            "是吗……\x01",
            "两人都很有精神，这就太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "看来正游击士的任务\x01",
            "都完成得很好嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E61")

    label("loc_E09")


    ChrTalk(    #50
        0xFE,
        (
            "听爱娜说了，艾丝蒂尔\x01",
            "也当上正游击士了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "哎呀哎呀，真是佩服。\x01",
            "干得很不错嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E61")


    ChrTalk(    #52
        0x101,
        (
            "#1008F嘿嘿……\x01",
            "嗯，目前为止是还不错啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "洛连特支部由于人手不足，\x01",
            "这阵子看来真是快忙翻了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "期待艾丝蒂尔\x01",
            "连卡西乌斯的份一起活跃啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1890)
    OP_A2(0x1)

    label("loc_EF8")

    Jump("loc_10C3")

    label("loc_EFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_10C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 4)), scpexpr(EXPR_END)), "loc_F7D")

    ChrTalk(    #55
        0xFE,
        (
            "政变是令人吃惊，\x01",
            "但从结果来说，或许\x01",
            "成为了王国整顿的契机。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "能够把光明的未来\x01",
            "托付给孩子们就最好不过了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C3")

    label("loc_F7D")


    ChrTalk(    #57
        0xFE,
        (
            "艾丝蒂尔……\x01",
            "几时回来的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        "#000F刚刚才到飞船坪呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "我听爱娜说了哦。\x01",
            "你也成为正游击士了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "看来这趟旅行\x01",
            "对你来说很有意义呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        "#008F嘿嘿，算是……吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "还听说卡西乌斯先生\x01",
            "也回到王国军去了，是吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "政变是令人吃惊，\x01",
            "但从结果来说，\x01",
            "或许倒是个契机。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "能够把光明的未来\x01",
            "托付给孩子们就最好不过了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1034)

    label("loc_10C3")

    TalkEnd(0xB)
    Return()

    # Function_4_4FE end

    def Function_5_10C7(): pass

    label("Function_5_10C7")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_1111")

    ChrTalk(    #65
        0xFE,
        (
            "真是的～爸爸又\x01",
            "开始自己胡乱担忧了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "我才７岁呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_154F")

    label("loc_1111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_11E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1194")

    ChrTalk(    #67
        0xFE,
        (
            "爸爸要出门，\x01",
            "所以尤妮看家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "不过，连灯也点不着，\x01",
            "一个人的话真有点害怕啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        "爸爸，早点回来……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_11DD")

    label("loc_1194")


    ChrTalk(    #70
        0xFE,
        (
            "房间的灯都点不着，\x01",
            "一个人的话真有点害怕……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "爸爸，早点回来……\x02",
    )

    CloseMessageWindow()

    label("loc_11DD")

    Jump("loc_154F")

    label("loc_11E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_122E")

    ChrTalk(    #72
        0xFE,
        (
            "嘿嘿，今天\x01",
            "一直和爸爸一起在哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "因为尤妮\x01",
            "最喜欢爸爸了嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_154F")

    label("loc_122E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_1325")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_127A")

    ChrTalk(    #74
        0xFE,
        "尤妮，要对爸爸道歉……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "我说爸爸……\x01",
            "『最坏』了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1322")

    label("loc_127A")


    ChrTalk(    #76
        0xFE,
        (
            "听说士兵们\x01",
            "在外面守着是真的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "外面那么危险\x01",
            "我一点儿也不知道……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "所以爸爸才不让\x01",
            "尤妮出去吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "……尤妮，要对爸爸道歉才行。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "说爸爸最坏了……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1322")

    Jump("loc_154F")

    label("loc_1325")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_137A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1348")

    ChrTalk(    #81
        0xFE,
        "爸爸好坏……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1377")

    label("loc_1348")


    ChrTalk(    #82
        0xFE,
        "爸爸好坏……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "人家以后不理他了啦。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1377")

    Jump("loc_154F")

    label("loc_137A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_1449")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_13BE")

    ChrTalk(    #84
        0xFE,
        (
            "就说今天一步\x01",
            "也不能出去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        "……爸爸真坏。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1446")

    label("loc_13BE")


    ChrTalk(    #86
        0xFE,
        "啊，艾丝蒂尔姐姐！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "嗯嗯，听我说啦。\x01",
            "爸爸好过分哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "竟然说尤妮\x01",
            "不能出门哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "我说这点雾不算什么啦，\x01",
            "他都完全不听。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1446")

    Jump("loc_154F")

    label("loc_1449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_154F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_14A2")

    ChrTalk(    #90
        0xFE,
        (
            "对了对了，姐姐，\x01",
            "见到鲁克了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "鲁克真是的，\x01",
            "总是说起姐姐哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_154F")

    label("loc_14A2")


    ChrTalk(    #92
        0xFE,
        "啊，艾丝蒂尔姐姐！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        "#001F尤妮，还好吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        "嗯，很好哦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "对了对了，姐姐，\x01",
            "见到鲁克了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "鲁克真是的，\x01",
            "总是说起姐姐哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        "#505F鲁克他？嗯…………\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_154F")

    TalkEnd(0xC)
    Return()

    # Function_5_10C7 end

    def Function_6_1553(): pass

    label("Function_6_1553")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_166D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_160D")

    ChrTalk(    #98
        0xFE,
        "唔唔……真奇怪。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "婚礼应该结束了，\x01",
            "女儿夫妇俩却还没回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "唔，在哪儿\x01",
            "耽搁了呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "哈哈哈。\x01",
            "算了，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "他们俩感情越好，\x01",
            "我就可以越快抱孙子啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_166A")

    label("loc_160D")


    ChrTalk(    #103
        0xFE,
        (
            "看来女儿夫妇俩\x01",
            "是在哪儿耽搁了吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "也好。\x01",
            "他们俩感情越好，\x01",
            "我就可以越快抱孙子了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_166A")

    Jump("loc_191E")

    label("loc_166D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_1762")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_170D")

    ChrTalk(    #105
        0xFE,
        "哎呀，有什么事呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "女儿夫妇俩去参加\x01",
            "礼拜堂的婚礼了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "新郎新娘接受\x01",
            "年轻夫妇的祝福……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "哈哈哈。\x01",
            "哎呀，多么美丽的一幕哟。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_175F")

    label("loc_170D")


    ChrTalk(    #109
        0xFE,
        (
            "女儿夫妇俩去参加\x01",
            "礼拜堂的婚礼了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "可是这种时候举行婚礼\x01",
            "真是有点可怜哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_175F")

    Jump("loc_191E")

    label("loc_1762")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_181B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_178F")

    ChrTalk(    #111
        0xFE,
        "哦，是你们啊。\x02",
    )

    CloseMessageWindow()

    label("loc_178F")


    ChrTalk(    #112
        0xFE,
        (
            "不知怎么的我家的导力器\x01",
            "都不能用了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        "这是故障吗？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1818")

    label("loc_17D2")


    ChrTalk(    #114
        0xFE,
        (
            "我家的导力器\x01",
            "不能动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "唔，稍后让胡里奥那家伙\x01",
            "去趟工房吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1818")

    Jump("loc_191E")

    label("loc_181B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_191E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1879")

    ChrTalk(    #116
        0xFE,
        "他还得多多学习些东西。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "继我之后，背负\x01",
            "洛连特林业重任的就只有他了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_191E")

    label("loc_1879")


    ChrTalk(    #118
        0xFE,
        (
            "神秘森林里\x01",
            "生长着塞尔贝的大树……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "传说以前\x01",
            "就有喜欢恶作剧的精灵在那居住。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "让人看见幻象，\x01",
            "在雾中迷失方向……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "嗯，就是类似\x01",
            "古老传说那样的东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_191E")

    TalkEnd(0x8)
    Return()

    # Function_6_1553 end

    def Function_7_1922(): pass

    label("Function_7_1922")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_19E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1973")

    ChrTalk(    #122
        0xFE,
        "这时候没工作真是帮大忙了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "这样我也能\x01",
            "照顾岳父了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19E5")

    label("loc_1973")


    ChrTalk(    #124
        0xFE,
        (
            "现在刚好植树造林\x01",
            "也告一段落了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "木材也没法出货，\x01",
            "目前暂时休业的状态。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "嗯，因此就能\x01",
            "照顾岳父了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_19E5")

    Jump("loc_1AA0")

    label("loc_19E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_1AA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1A3A")

    ChrTalk(    #127
        0xFE,
        (
            "岳父的睡着的样子\x01",
            "看来非常幸福呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        "到底做着怎样的梦呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AA0")

    label("loc_1A3A")


    ChrTalk(    #129
        0xFE,
        "啊，今天也来了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "岳父还是\x01",
            "没有醒过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "只有一点欣慰的是\x01",
            "他的睡脸\x01",
            "看起来相当幸福。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1AA0")

    TalkEnd(0xA)
    Return()

    # Function_7_1922 end

    def Function_8_1AA4(): pass

    label("Function_8_1AA4")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_1DAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34B, 4)), scpexpr(EXPR_END)), "loc_1BA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B43")

    ChrTalk(    #132
        0xFE,
        (
            "父亲真是的，一醒来\x01",
            "就让老公去工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "一整晚都照看着他，\x01",
            "还突然让人家工作……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "就算关系好了\x01",
            "一提到工作还是那么严厉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BA6")

    label("loc_1B43")


    ChrTalk(    #135
        0xFE,
        (
            "此次一切\x01",
            "都承蒙关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "父亲的情况我们\x01",
            "也会多加注意的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "那么，你们也\x01",
            "要多加小心哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BA6")

    Jump("loc_1DAA")

    label("loc_1BA9")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #138
        0xFE,
        "啊，是你们……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "太好了，父亲平安\x01",
            "醒过来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "真的……\x01",
            "不知道该怎么感谢你们才好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        "#1025F不用，别这么客气……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x103,
        "#020F那么，令尊的情况如何？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #143
        0xFE,
        "嗯，非常精神哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "虽然还有点迷糊，\x01",
            "但我想很快就会好的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        "#1011F是吗……看来没事呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x103,
        (
            "#026F是啊，我想应该没事了……\x02\x03",

            "#020F不过如果有什么变化\x01",
            "请立即联系教区长吧。\x02\x03",

            "他应该会告知\x01",
            "适当的应对方法的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "嗯，谢谢。\x01",
            "我们会注意观察的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "……你们也是，\x01",
            "要多加小心哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x101,
        "#1006F嗯，谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x103,
        "#020F……那么，先告辞了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A5C)
    OP_A2(0x5)

    label("loc_1DAA")

    Jump("loc_20D4")

    label("loc_1DAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_1EB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1E27")

    ChrTalk(    #151
        0xFE,
        (
            "这么担心父亲\x01",
            "真是令人感激……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "这样下去说不定\x01",
            "他才让我更伤脑筋呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "今天可得\x01",
            "换我来照顾了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EB4")

    label("loc_1E27")


    ChrTalk(    #154
        0xFE,
        (
            "老公也是不眠不休地\x01",
            "照料着父亲呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "我说换我来，\x01",
            "他都不肯离开……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "这样下去\x01",
            "他才让我更伤脑筋呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "今天可得\x01",
            "换我来照顾了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1EB4")

    Jump("loc_20D4")

    label("loc_1EB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_1F9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1F10")

    ChrTalk(    #158
        0xFE,
        (
            "雾看起来好像\x01",
            "比昨天更浓了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "不管怎样，希望\x01",
            "别再发生任何事了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F97")

    label("loc_1F10")


    ChrTalk(    #160
        0xFE,
        (
            "雾看起来好像\x01",
            "比昨天更浓了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "父亲仍旧\x01",
            "在安睡着……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "不管怎样，希望\x01",
            "别再发生任何事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "女神啊……\x01",
            "求求你救救他吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1F97")

    Jump("loc_20D4")

    label("loc_1F9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_2072")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1FEF")

    ChrTalk(    #164
        0xFE,
        (
            "父亲最近也\x01",
            "接受了老公。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "……事情太顺利\x01",
            "甚至觉得有点可怕。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_206F")

    label("loc_1FEF")


    ChrTalk(    #166
        0xFE,
        (
            "老公胡里奥，以前\x01",
            "只知道拼命工作的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "最近却感觉好像\x01",
            "沉着稳重多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "和父亲也相处得很好，\x01",
            "是抓住了工作要领吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_206F")

    Jump("loc_20D4")

    label("loc_2072")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_20D4")

    ChrTalk(    #169
        0xFE,
        "老公的工作非常顺利。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "和父亲也相处得很好，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        "……我现在非常幸福。\x02",
    )

    CloseMessageWindow()

    label("loc_20D4")

    TalkEnd(0x9)
    Return()

    # Function_8_1AA4 end

    def Function_9_20D8(): pass

    label("Function_9_20D8")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_227E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_21DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_213A")

    ChrTalk(    #172
        0xF,
        (
            "那么，委任书的事\x01",
            "就拜托你们了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xF,
        (
            "如果找到了，\x01",
            "就马上回来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D9")

    label("loc_213A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2192")

    ChrTalk(    #174
        0xF,
        (
            "委任书的事……\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xF,
        (
            "因为这件事，我担心得\x01",
            "都没心思工作了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D9")

    label("loc_2192")


    ChrTalk(    #176
        0xF,
        (
            "啊，游击士。\x01",
            "调查有进展吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xF,
        (
            "委任书的事……\x01",
            "就拜托你们了！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_21D9")

    Jump("loc_227B")

    label("loc_21DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_21FF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_21F8")
    Call(1, 1)
    Jump("loc_21FC")

    label("loc_21F8")

    Call(1, 0)

    label("loc_21FC")

    Jump("loc_227B")

    label("loc_21FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2223")

    ChrTalk(    #178
        0xF,
        "唔～～……真伤脑筋。\x02",
    )

    CloseMessageWindow()
    Jump("loc_227B")

    label("loc_2223")


    ChrTalk(    #179
        0xF,
        "唔～～……真伤脑筋。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xF,
        (
            "好不容易到了要重新开工的时候，\x01",
            "那东西却偏偏不见了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_227B")

    Jump("loc_253A")

    label("loc_227E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_23C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_22E5")

    ChrTalk(    #181
        0xF,
        (
            "山道出现了雾样的妖怪\x01",
            "真是给吓了一大跳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xF,
        (
            "游击士小哥用剑一砍，\x01",
            "就烟消云散了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23BE")

    label("loc_22E5")


    ChrTalk(    #183
        0xF,
        (
            "真伤脑筋……\x01",
            "雾居然到山上来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xF,
        (
            "工作没法继续，\x01",
            "只能盲目等待时，\x01",
            "协会发来了联络。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xF,
        (
            "说派了游击士来，\x01",
            "所以就被护送回了城。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xF,
        (
            "从山道回来时，好几次\x01",
            "被雾妖袭击。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xF,
        (
            "如果游击士没来，\x01",
            "当真是危在旦夕啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_23BE")

    Jump("loc_253A")

    label("loc_23C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_253A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 2)), scpexpr(EXPR_END)), "loc_2411")

    ChrTalk(    #188
        0xF,
        "今天是陪伴家人的日子。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xF,
        (
            "最近由于工作\x01",
            "一直窝在矿山里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_253A")

    label("loc_2411")


    ChrTalk(    #190
        0xF,
        "……啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xF,
        (
            "这不是以前承蒙照顾的\x01",
            "游击士小姑娘吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        "#501F啊，玛鲁加矿山的工头……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xF,
        (
            "多亏了你们，\x01",
            "新矿脉的开采很顺利哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xF,
        (
            "在那之后，最后用炸药把\x01",
            "魔兽出现的洞穴堵上了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x101,
        "#506F真，真是…啊哈哈…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xF,
        "嗯，没有其它办法了嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xF,
        (
            "但是，多亏这个办法，\x01",
            "现在的玛鲁加矿山景气多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1032)

    label("loc_253A")

    TalkEnd(0xF)
    Return()

    # Function_9_20D8 end

    def Function_10_253E(): pass

    label("Function_10_253E")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_2653")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25FE")

    ChrTalk(    #198
        0xFE,
        (
            "就在刚才\x01",
            "老公突然回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "好像出了些麻烦事，\x01",
            "但矿山的工作还是在继续。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "这种时候，\x01",
            "早点回来多好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "唉，他那人性格就是这样，\x01",
            "无论怎么劝阻也是没用的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_2650")

    label("loc_25FE")


    ChrTalk(    #202
        0xFE,
        (
            "刚才老公\x01",
            "从矿山回来了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "好像出了些麻烦事，\x01",
            "但今天好像还要继续工作呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2650")

    Jump("loc_2C2A")

    label("loc_2653")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2722")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26D5")

    ChrTalk(    #204
        0xFE,
        (
            "导力器都停止了，\x01",
            "真的很让人担心啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "正好矿山\x01",
            "才刚刚开始工程。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "别发生什么\x01",
            "事故或麻烦就好……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_271F")

    label("loc_26D5")


    ChrTalk(    #207
        0xFE,
        (
            "导力器都停止了，\x01",
            "真的很让人担心啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "正好矿山\x01",
            "才刚刚开始工程。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_271F")

    Jump("loc_2C2A")

    label("loc_2722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_2932")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_284C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2789")

    ChrTalk(    #209
        0xFE,
        (
            "他那么努力\x01",
            "也是为了我们家人嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "我也要尽一切力量，\x01",
            "支撑老公才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2849")

    label("loc_2789")


    ChrTalk(    #211
        0xFE,
        (
            "天刚晴\x01",
            "马上就重新开工……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "玛鲁加矿山\x01",
            "现在好像非常忙碌呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        (
            "都起了那么大的雾，\x01",
            "稍微休息下就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "但是，他那么努力\x01",
            "也是为了我们家人嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "想到这个，\x01",
            "也不能有怨言了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_2849")

    Jump("loc_292F")

    label("loc_284C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_28A2")

    ChrTalk(    #216
        0xFE,
        (
            "老公好像\x01",
            "给你们添麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "不管怎样，能够平安\x01",
            "看他出门真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_292F")

    label("loc_28A2")


    ChrTalk(    #218
        0xFE,
        (
            "我家老公，今天应该\x01",
            "开始矿山的工作了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        (
            "但现在还没出去呢，\x01",
            "好像丢了什么重要的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "真是的，其他矿工们的\x01",
            "监督工作不要紧吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_292F")

    Jump("loc_2C2A")

    label("loc_2932")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_2A1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2991")

    ChrTalk(    #221
        0xFE,
        (
            "不管怎样，老公平安\x01",
            "回来就比什么都重要了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "这些还都\x01",
            "多亏了游击士们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A17")

    label("loc_2991")


    ChrTalk(    #223
        0xFE,
        (
            "啊啊，太好了……\x01",
            "老公平安从矿山回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "好像是游击士们\x01",
            "一直护卫到城里来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "雾居然都到了矿山……\x01",
            "到底是怎么回事呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_2A17")

    Jump("loc_2C2A")

    label("loc_2A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_2AD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2A64")

    ChrTalk(    #226
        0xFE,
        (
            "老公平安\x01",
            "到达矿山了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        "别在路上迷路就好了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AD5")

    label("loc_2A64")


    ChrTalk(    #228
        0xFE,
        (
            "不得了了……\x01",
            "今天早上雾不是也很大吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "真担心老公……\x01",
            "平安到达矿山了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xFE,
        "别在路上迷路就好了……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_2AD5")

    Jump("loc_2C2A")

    label("loc_2AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_2BF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2B5E")

    ChrTalk(    #231
        0xFE,
        (
            "也许因为很少见面，\x01",
            "我家女儿和爸爸很亲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "因此\x01",
            "我们夫妇也很圆满。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "和他在一起１５年，\x01",
            "都还没到疲劳期呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BF1")

    label("loc_2B5E")


    ChrTalk(    #234
        0xFE,
        (
            "老公去矿山\x01",
            "已经４天了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "差不多是女儿开始\x01",
            "想爸爸的时候了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "也许因为很少相见，\x01",
            "真是个亲爸爸的孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "因此\x01",
            "我们夫妇也很圆满。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_2BF1")

    Jump("loc_2C2A")

    label("loc_2BF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_2C2A")

    ChrTalk(    #238
        0xFE,
        (
            "今天大家要一起出门，\x01",
            "所以正在准备便当呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C2A")

    TalkEnd(0xD)
    Return()

    # Function_10_253E end

    def Function_11_2C2E(): pass

    label("Function_11_2C2E")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_2C70")

    ChrTalk(    #239
        0xFE,
        "刚才爸爸回来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        (
            "但是，马上又\x01",
            "去工作了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_302B")

    label("loc_2C70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2CBC")

    ChrTalk(    #241
        0xFE,
        (
            "妈妈也真是的，\x01",
            "到底在想什么嘛～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        (
            "是不是\x01",
            "有什么烦心事呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_302B")

    label("loc_2CBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_2D5E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2D24")

    ChrTalk(    #243
        0xFE,
        (
            "啊……爸爸\x01",
            "又去工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xFE,
        (
            "这次的工作\x01",
            "要去几天呢～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        "希望他早点回来……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D5B")

    label("loc_2D24")


    ChrTalk(    #246
        0xFE,
        (
            "总觉得爸爸\x01",
            "一脸烦恼的样子～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        "怎～么回事呢……\x02",
    )

    CloseMessageWindow()

    label("loc_2D5B")

    Jump("loc_302B")

    label("loc_2D5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_2E38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2DBB")

    ChrTalk(    #248
        0xFE,
        (
            "红头发的哥哥他们\x01",
            "把爸爸带回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "嘿嘿……爸爸\x01",
            "回来我真好高兴喔⊙\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E35")

    label("loc_2DBB")


    ChrTalk(    #250
        0xFE,
        (
            "红头发哥哥他们\x01",
            "把爸爸带回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        (
            "听说矿山也起了雾，\x01",
            "所以回来避难的～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "嘿嘿……不过，爸爸\x01",
            "回来我好高兴喔⊙\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_2E35")

    Jump("loc_302B")

    label("loc_2E38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_2EEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2E93")

    ChrTalk(    #253
        0xFE,
        (
            "爸爸总是\x01",
            "一早就出去工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        (
            "阿妮娅也起得很早，\x01",
            "可总是见不到爸爸。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EEC")

    label("loc_2E93")


    ChrTalk(    #255
        0xFE,
        (
            "爸爸总是\x01",
            "一早就出去工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "阿妮娅也起得很早，\x01",
            "可总是见不到爸爸。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        "呜……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_2EEC")

    Jump("loc_302B")

    label("loc_2EEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_2FE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2F4A")

    ChrTalk(    #258
        0xFE,
        (
            "阿妮娅已经\x01",
            "好～久没见到爸爸了啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        (
            "好想爸爸～\x01",
            "然后再一起去郊游。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FDD")

    label("loc_2F4A")


    ChrTalk(    #260
        0xFE,
        (
            "爸爸的工作\x01",
            "现在非常忙哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        (
            "阿妮娅已经\x01",
            "好～久没见到爸爸了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        (
            "呜～呜，前阵子的\x01",
            "郊游好开心哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        (
            "好想再和爸爸一起\x01",
            "去帕赛尔农场哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_2FDD")

    Jump("loc_302B")

    label("loc_2FE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_302B")

    ChrTalk(    #264
        0xFE,
        (
            "嘿嘿，今天\x01",
            "爸爸说他放假。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "所以就带我去\x01",
            "帕赛尔农场郊游了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_302B")

    TalkEnd(0xE)
    Return()

    # Function_11_2C2E end

    def Function_12_302F(): pass

    label("Function_12_302F")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x8, -42510, 0, 37680, 238)
    SetChrPos(0x9, -43770, 0, 36860, 59)
    SetChrPos(0xA, -43000, 0, 36530, 10)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_6F(0x2, 0)
    OP_6D(-39410, 0, 35550, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)

    def lambda_30EB():
        OP_6D(-43060, 0, 37080, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_30EB)
    Sleep(1500)
    OP_62(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_95(0x8, 0x0, 0x0, 0x0, 0xC8, 0xFA0)
    Sleep(500)
    OP_8C(0x8, 180, 400)
    OP_8C(0x8, 90, 400)
    OP_8C(0x8, 0, 400)
    OP_8C(0x8, 270, 400)
    OP_8C(0x8, 238, 400)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0410   ._SN", 110, 0, 0)
    IdleLoop()
    Return()

    # Function_12_302F end

    SaveToFile()

Try(main)
