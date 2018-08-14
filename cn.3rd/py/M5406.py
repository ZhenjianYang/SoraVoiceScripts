from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M5406   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5406.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60234",
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
        '多伦',                                 # 9
        '吉尔',                                 # 10
        '空贼',                                 # 11
        '空贼',                                 # 12
        '空贼',                                 # 13
        '空贼',                                 # 14
        '空贼',                                 # 15
        '空贼',                                 # 16
        '',                                     # 17
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
        'ED6_DT07/CH02110 ._CH',             # 00
        'ED6_DT07/CH00290 ._CH',             # 01
        'ED6_DT07/CH00291 ._CH',             # 02
        'ED6_DT07/CH02120 ._CH',             # 03
        'ED6_DT07/CH00300 ._CH',             # 04
        'ED6_DT07/CH00301 ._CH',             # 05
        'ED6_DT07/CH00360 ._CH',             # 06
        'ED6_DT07/CH00361 ._CH',             # 07
        'ED6_DT07/CH00294 ._CH',             # 08
        'ED6_DT07/CH00304 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH02110P._CP',             # 00
        'ED6_DT07/CH00290P._CP',             # 01
        'ED6_DT07/CH00291P._CP',             # 02
        'ED6_DT07/CH02120P._CP',             # 03
        'ED6_DT07/CH00300P._CP',             # 04
        'ED6_DT07/CH00301P._CP',             # 05
        'ED6_DT07/CH00360P._CP',             # 06
        'ED6_DT07/CH00361P._CP',             # 07
        'ED6_DT07/CH00294P._CP',             # 08
        'ED6_DT07/CH00304P._CP',             # 09
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x0,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -3720,
        Y                   = -2000,
        Z                   = -4000,
        Range               = 5440,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )


    ScpFunction(
        "Function_0_21A",          # 00, 0
        "Function_1_237",          # 01, 1
        "Function_2_238",          # 02, 2
        "Function_3_249",          # 03, 3
        "Function_4_1D7F",         # 04, 4
        "Function_5_1DCE",         # 05, 5
        "Function_6_1E1D",         # 06, 6
        "Function_7_1E6C",         # 07, 7
        "Function_8_1EBB",         # 08, 8
        "Function_9_1F0A",         # 09, 9
        "Function_10_1F59",        # 0A, 10
        "Function_11_2674",        # 0B, 11
        "Function_12_3516",        # 0C, 12
    )


    def Function_0_21A(): pass

    label("Function_0_21A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_236")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 11)

    label("loc_236")

    Return()

    # Function_0_21A end

    def Function_1_237(): pass

    label("Function_1_237")

    Return()

    # Function_1_237 end

    def Function_2_238(): pass

    label("Function_2_238")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 7)), scpexpr(EXPR_END)), "loc_240")
    Return()

    label("loc_240")

    Call(0, 3)
    Call(0, 10)
    Return()

    # Function_2_238 end

    def Function_3_249(): pass

    label("Function_3_249")

    EventBegin(0x0)
    OP_20(0x7D0)
    LoadEffect(0x0, "map\\mp250_00.eff")
    LoadEffect(0x1, "map\\mp250_01.eff")
    LoadEffect(0x2, "monster\\msc1000.eff")
    OP_E0(238, 0x4A, 0x2)
    OP_E0(238, 0x4B, 0x3)
    OP_E0(239, 0x4C, 0x2)
    OP_E0(239, 0x4D, 0x3)
    OP_E0(240, 0x4E, 0x2)
    OP_E0(240, 0x4F, 0x3)
    OP_E0(241, 0x50, 0x2)
    OP_E0(241, 0x51, 0x3)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 1600, -1000, 15930, 180)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -30, -1000, 15930, 180)
    SetChrSubChip(0x11, 0)
    Sleep(500)

    NpcTalk(    #0
        0x10,
        "男子的声音",
        (
            "#4P#4S嘎哈哈！\x01",
            "终于来了啊！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35B")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3C2")

    label("loc_35B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_383")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3C2")

    label("loc_383")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AB")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3C2")

    label("loc_3AB")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EA")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_451")

    label("loc_3EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_412")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_451")

    label("loc_412")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43A")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_451")

    label("loc_43A")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_451")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_479")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4E0")

    label("loc_479")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A1")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4E0")

    label("loc_4A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C9")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4E0")

    label("loc_4C9")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_508")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_56F")

    label("loc_508")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_530")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_56F")

    label("loc_530")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_558")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_56F")

    label("loc_558")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_56F")

    Sleep(1000)

    def lambda_57A():
        OP_6D(1840, -1000, 16610, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_57A)

    def lambda_592():
        OP_67(0, 6000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_592)

    def lambda_5AA():
        OP_6B(3730, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_5AA)

    def lambda_5BA():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_5BA)

    def lambda_5CA():
        OP_6E(210, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_5CA)

    def lambda_5DA():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_5DA)

    def lambda_5E8():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_5E8)

    def lambda_5F6():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF0, 3, lambda_5F6)

    def lambda_604():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_604)
    WaitChrThread(0xEE, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_639")

    ChrTalk(    #1
        0x10B,
        "#216F啊……！\x02",
    )

    CloseMessageWindow()

    label("loc_639")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_660")

    ChrTalk(    #2
        0x101,
        "#1004F哎……\x02",
    )

    CloseMessageWindow()

    label("loc_660")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_689")

    ChrTalk(    #3
        0x103,
        "#1523F哎呀……\x02",
    )

    CloseMessageWindow()

    label("loc_689")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B1")

    ChrTalk(    #4
        0x106,
        "#055F喂喂……\x02",
    )

    CloseMessageWindow()

    label("loc_6B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D9")

    ChrTalk(    #5
        0x108,
        "#071F哈哈……\x02",
    )

    CloseMessageWindow()

    label("loc_6D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6FF")

    ChrTalk(    #6
        0x10C,
        "#113F哦……\x02",
    )

    CloseMessageWindow()

    label("loc_6FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_726")

    ChrTalk(    #7
        0x105,
        "#1164F啊……\x02",
    )

    CloseMessageWindow()

    label("loc_726")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74E")

    ChrTalk(    #8
        0x10E,
        "#173F难道……\x02",
    )

    CloseMessageWindow()

    label("loc_74E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_77B")

    ChrTalk(    #9
        0x104,
        "#1541F这、这是……\x02",
    )

    CloseMessageWindow()

    label("loc_77B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A5")

    ChrTalk(    #10
        0x107,
        "#065F哎……！？\x02",
    )

    CloseMessageWindow()

    label("loc_7A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7D1")

    ChrTalk(    #11
        0x10D,
        "#273F……唔………\x02",
    )

    CloseMessageWindow()

    label("loc_7D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7FE")

    ChrTalk(    #12
        0x10A,
        "#1317F那、那个……\x02",
    )

    CloseMessageWindow()

    label("loc_7FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_823")

    ChrTalk(    #13
        0x110,
        "#1305F唔？\x02",
    )

    CloseMessageWindow()

    label("loc_823")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_84A")

    ChrTalk(    #14
        0x10F,
        "#1444F？？？\x02",
    )

    CloseMessageWindow()

    label("loc_84A")


    ChrTalk(    #15
        0x102,
        "#1504F多伦兄，吉尔兄！？\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6D(2180, -1000, 12120, 0)
    OP_67(0, 4890, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(341, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CB0")
    SetChrPos(0x109, 40, -1000, -2040, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_955")
    SetChrPos(0xEF, 1620, -1000, -310, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_922")
    SetChrPos(0xF0, 340, -1000, 800, 0)
    SetChrPos(0xF1, 1880, -1000, -2820, 0)
    Jump("loc_952")

    label("loc_922")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_952")
    SetChrPos(0xF1, 340, -1000, 800, 0)
    SetChrPos(0xF0, 1880, -1000, -2820, 0)

    label("loc_952")

    Jump("loc_A5C")

    label("loc_955")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9DA")
    SetChrPos(0xF0, 1620, -1000, -310, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A7")
    SetChrPos(0xEF, 340, -1000, 800, 0)
    SetChrPos(0xF1, 1880, -1000, -2820, 0)
    Jump("loc_9D7")

    label("loc_9A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D7")
    SetChrPos(0xF1, 340, -1000, 800, 0)
    SetChrPos(0xEF, 1880, -1000, -2820, 0)

    label("loc_9D7")

    Jump("loc_A5C")

    label("loc_9DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5C")
    SetChrPos(0xF1, 1620, -1000, -310, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2C")
    SetChrPos(0xEF, 340, -1000, 800, 0)
    SetChrPos(0xF0, 1880, -1000, -2820, 0)
    Jump("loc_A5C")

    label("loc_A2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5C")
    SetChrPos(0xF0, 340, -1000, 800, 0)
    SetChrPos(0xEF, 1880, -1000, -2820, 0)

    label("loc_A5C")


    def lambda_A62():
        OP_8F(0xFE, 0xFFFFFF60, 0xFFFFFC18, 0x17FC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A62)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2E")

    def lambda_A8B():
        OP_8F(0xFE, 0x64A, 0xFFFFFC18, 0x1E0A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_A8B)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE7")

    def lambda_AB4():
        OP_8F(0xFE, 0x64, 0xFFFFFC18, 0x1EDC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_AB4)

    def lambda_ACF():
        OP_8F(0xFE, 0x690, 0xFFFFFC18, 0x172A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_ACF)
    Jump("loc_B2B")

    label("loc_AE7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2B")

    def lambda_AFB():
        OP_8F(0xFE, 0x64, 0xFFFFFC18, 0x1EDC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_AFB)

    def lambda_B16():
        OP_8F(0xFE, 0x690, 0xFFFFFC18, 0x172A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_B16)

    label("loc_B2B")

    Jump("loc_C99")

    label("loc_B2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE5")

    def lambda_B42():
        OP_8F(0xFE, 0x64A, 0xFFFFFC18, 0x1E0A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_B42)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B9E")

    def lambda_B6B():
        OP_8F(0xFE, 0x64, 0xFFFFFC18, 0x1EDC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_B6B)

    def lambda_B86():
        OP_8F(0xFE, 0x690, 0xFFFFFC18, 0x172A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_B86)
    Jump("loc_BE2")

    label("loc_B9E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE2")

    def lambda_BB2():
        OP_8F(0xFE, 0x64, 0xFFFFFC18, 0x1EDC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_BB2)

    def lambda_BCD():
        OP_8F(0xFE, 0x690, 0xFFFFFC18, 0x172A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_BCD)

    label("loc_BE2")

    Jump("loc_C99")

    label("loc_BE5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C99")

    def lambda_BF9():
        OP_8F(0xFE, 0x64A, 0xFFFFFC18, 0x1E0A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_BF9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C55")

    def lambda_C22():
        OP_8F(0xFE, 0x64, 0xFFFFFC18, 0x1EDC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_C22)

    def lambda_C3D():
        OP_8F(0xFE, 0x690, 0xFFFFFC18, 0x172A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_C3D)
    Jump("loc_C99")

    label("loc_C55")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C99")

    def lambda_C69():
        OP_8F(0xFE, 0x64, 0xFFFFFC18, 0x1EDC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_C69)

    def lambda_C84():
        OP_8F(0xFE, 0x690, 0xFFFFFC18, 0x172A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_C84)

    label("loc_C99")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    Jump("loc_EC8")

    label("loc_CB0")

    SetChrPos(0x109, 1620, -1000, -310, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D05")
    SetChrPos(0xEF, 340, -1000, 800, 0)
    SetChrPos(0xF0, 40, -1000, -2040, 0)
    SetChrPos(0xF1, 1880, -1000, -2820, 0)
    Jump("loc_D8A")

    label("loc_D05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D49")
    SetChrPos(0xF0, 340, -1000, 800, 0)
    SetChrPos(0xEF, 40, -1000, -2040, 0)
    SetChrPos(0xF1, 1880, -1000, -2820, 0)
    Jump("loc_D8A")

    label("loc_D49")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D8A")
    SetChrPos(0xF1, 340, -1000, 800, 0)
    SetChrPos(0xEF, 40, -1000, -2040, 0)
    SetChrPos(0xF0, 1880, -1000, -2820, 0)

    label("loc_D8A")


    def lambda_D90():
        OP_8F(0xFE, 0x64A, 0xFFFFFC18, 0x1E0A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E07")

    def lambda_DB9():
        OP_8F(0xFE, 0x0, 0xFFFFFC18, 0x1EDC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_DB9)

    def lambda_DD4():
        OP_8F(0xFE, 0xFFFFFF60, 0xFFFFFC18, 0x17FC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_DD4)

    def lambda_DEF():
        OP_8F(0xFE, 0x690, 0xFFFFFC18, 0x172A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_DEF)
    Jump("loc_EC8")

    label("loc_E07")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E69")

    def lambda_E1B():
        OP_8F(0xFE, 0x0, 0xFFFFFC18, 0x1EDC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_E1B)

    def lambda_E36():
        OP_8F(0xFE, 0xFFFFFF60, 0xFFFFFC18, 0x17FC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_E36)

    def lambda_E51():
        OP_8F(0xFE, 0x690, 0xFFFFFC18, 0x172A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_E51)
    Jump("loc_EC8")

    label("loc_E69")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC8")

    def lambda_E7D():
        OP_8F(0xFE, 0x0, 0xFFFFFC18, 0x1EDC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_E7D)

    def lambda_E98():
        OP_8F(0xFE, 0xFFFFFF60, 0xFFFFFC18, 0x17FC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_E98)

    def lambda_EB3():
        OP_8F(0xFE, 0x690, 0xFFFFFC18, 0x172A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_EB3)

    label("loc_EC8")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F61")

    ChrTalk(    #16
        0x10B,
        (
            "#415F#6P慢、慢着！\x01",
            "为什么哥哥们会……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #17
        0x10B,
        "#216F#6P难、难不成……\x02",
    )

    CloseMessageWindow()

    label("loc_F61")


    ChrTalk(    #18
        0x109,
        (
            "#1063F#12P看来你们\x01",
            "也被利用了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        (
            "#198F#5P哦哦，说得没错。\x02\x03",

            "#490F虽然不太清楚状况，\x01",
            "但『就是这么回事』的感觉\x01",
            "却不言而喻啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x11,
        (
            "#204F#5P既然如此，\x01",
            "就让这种无聊的事情赶快结束了吧。\x02\x03",

            "#200F这样比较痛快吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11C3")

    ChrTalk(    #21
        0x10B,
        "#216F#6P慢、慢着！\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #22
        0x10B,
        (
            "#418F#6P竟然要和哥哥们作战……\x01",
            "我怎么能干啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        (
            "#198F#5P哎呀，\x01",
            "都说我们不是真人啦。\x02\x03",

            "#197F是『影之王』那个混帐\x01",
            "做出来的假货而已啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x11,
        (
            "#203F#5P证据就是，\x01",
            "似乎面对你也不会手下留情……\x02\x03",

            "#206F不用客气啦。\x01",
            "打起精神放马过来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10B,
        "#417F#6P这、这么说也太……！\x02",
    )

    CloseMessageWindow()

    label("loc_11C3")


    ChrTalk(    #26
        0x102,
        "#1503F#12P吉尔兄，多伦兄……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x11,
        (
            "#202F#5P约修亚，好久不见啊。\x02\x03",

            "#200F听说你去旅行了……\x01",
            "还好吗？\x02",
        )
    )

    Jump("loc_1249")

    label("loc_1249")

    CloseMessageWindow()

    ChrTalk(    #28
        0x102,
        (
            "#1513F#12P嗯……托你们的福。\x02\x03",

            "#1501F你们的运输公司\x01",
            "似乎也很顺利，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "#198F#5P哎，欠了女王的债，\x01",
            "不早点还钱不行啊。\x02\x03",

            "#490F为了这个，\x01",
            "你们可要赶快解决这个事件，\x01",
            "让乔丝特平安回来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x11,
        (
            "#203F#5P毕竟她是我们的经理负责人啊。\x02\x03",

            "要是就这样回不来了，\x01",
            "我们不到一个月肯定饿死。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        "#1509F#12P哈哈，确实是呢。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_146A")

    ChrTalk(    #32
        0x10B,
        (
            "#413F#6P吉尔哥，多伦哥……\x02\x03",

            "#212F明白了……\x01",
            "我会尽全力加油的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x11,
        (
            "#202F#5P啊啊，就是这种气势。\x02\x03",

            "#200F那么……\x01",
            "赶快开始吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1494")

    label("loc_146A")


    ChrTalk(    #34
        0x10,
        (
            "#191F#5P好，\x01",
            "那么赶快开始吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1494")

    Sleep(300)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x11, 4)
    SetChrSubChip(0x11, 0)
    OP_0D()
    Sleep(300)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, -100, -900, 18500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xFF, 1910, -900, 18500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0xFF, -2700, -900, 15870, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x4, 0xFF, 4200, -900, 16059, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x5, 0xFF, -110, -900, 13340, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x6, 0xFF, 2000, -900, 13110, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_1615():
        OP_6D(1910, -1000, 12760, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1615)

    def lambda_162D():
        OP_67(0, 6230, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_162D)

    def lambda_1645():
        OP_6B(3170, 3000)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1645)

    def lambda_1655():
        OP_6E(310, 3000)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1655)
    OP_0D()
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x12, -100, -4000, 18500, 180)
    SetChrPos(0x13, 1910, -4000, 18500, 180)
    SetChrPos(0x14, -2700, -4000, 15870, 180)
    SetChrPos(0x15, 4200, -4000, 16059, 180)
    SetChrPos(0x16, -110, -4000, 13340, 180)
    SetChrPos(0x17, 2000, -4000, 13110, 180)
    OP_22(0x85, 0x1, 0x64)

    def lambda_16EF():

        label("loc_16EF")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_16EF")

    QueueWorkItem2(0x109, 3, lambda_16EF)
    OP_43(0x12, 0x0, 0x0, 0x4)
    OP_43(0x13, 0x0, 0x0, 0x5)
    OP_43(0x14, 0x0, 0x0, 0x6)
    OP_43(0x15, 0x0, 0x0, 0x7)
    OP_43(0x16, 0x0, 0x0, 0x8)
    OP_43(0x17, 0x0, 0x0, 0x9)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1772")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_17D9")

    label("loc_1772")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_179A")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_17D9")

    label("loc_179A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17C2")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_17D9")

    label("loc_17C2")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_17D9")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1806")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_186D")

    label("loc_1806")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_182E")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_186D")

    label("loc_182E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1856")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_186D")

    label("loc_1856")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_186D")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_189A")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1901")

    label("loc_189A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18C2")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1901")

    label("loc_18C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18EA")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1901")

    label("loc_18EA")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1901")

    Sleep(1000)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 10)
    SetChrSubChip(0x109, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 12)
    SetChrSubChip(0xEF, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 14)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 16)
    SetChrSubChip(0xF1, 0)
    OP_0D()
    Sleep(300)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x13, 0x0)
    WaitChrThread(0x14, 0x0)
    WaitChrThread(0x15, 0x0)
    WaitChrThread(0x16, 0x0)
    WaitChrThread(0x17, 0x0)
    OP_44(0x109, 0x3)
    OP_23(0x85)
    OP_1D(0xC4)
    Fade(1000)
    OP_82(0x0, 0x0)
    LoadEffect(0x1, "map\\mp250_00.eff")
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    OP_82(0x5, 0x0)
    OP_82(0x6, 0x0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19E7")

    ChrTalk(    #35
        0x10B,
        "#216F#6P……大家……！\x02",
    )

    CloseMessageWindow()

    label("loc_19E7")


    ChrTalk(    #36
        0x109,
        (
            "#1840F#12P哎呀哎呀……\x01",
            "这么痛快，真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10,
        (
            "#196F#5P卡普亚特急便社长，\x01",
            "多伦·卡普亚！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x11,
        (
            "#201F#5P同公司副社长，\x01",
            "吉尔·卡普亚！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(80, 120, -1, -1)
    SetChrName("原空贼们")

    AnonymousTalk(    #39
        "\x07\x00#4S以及全体社员！\x02",
    )

    Jump("loc_1ACC")

    label("loc_1ACC")

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)

    ChrTalk(    #40
        0x11,
        (
            "#206F正如刚才所说，\x01",
            "我们不会手下留情的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10,
        (
            "#196F大家都要\x01",
            "尽全力一战哦！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B72")

    ChrTalk(    #42
        0x10B,
        "#214F#6P嗯……！\x02",
    )

    CloseMessageWindow()

    label("loc_1B72")


    ChrTalk(    #43
        0x102,
        "#1506F#12P那么上吧！\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1BA7():
        OP_6D(1840, -1000, 12320, 250)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1BA7)

    def lambda_1BBF():
        OP_67(0, 6580, -10000, 250)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_1BBF)

    def lambda_1BD7():
        OP_6B(2900, 250)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_1BD7)

    def lambda_1BE7():
        OP_6E(240, 250)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_1BE7)
    SetChrChipByIndex(0x10, 2)

    def lambda_1BFC():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1BFC)
    SetChrChipByIndex(0x11, 5)

    def lambda_1C1C():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1C1C)
    SetChrChipByIndex(0x12, 7)

    def lambda_1C3C():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1C3C)
    SetChrChipByIndex(0x13, 7)

    def lambda_1C5C():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1C5C)
    SetChrChipByIndex(0x14, 7)

    def lambda_1C7C():
        OP_8E(0xFE, 0xF0, 0xFFFFFC18, 0x31E2, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1C7C)
    SetChrChipByIndex(0x15, 7)

    def lambda_1C9C():
        OP_8E(0xFE, 0x5BE, 0xFFFFFC18, 0x3174, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1C9C)
    SetChrChipByIndex(0x16, 7)

    def lambda_1CBC():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_1CBC)
    SetChrChipByIndex(0x17, 7)

    def lambda_1CDC():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_1CDC)

    def lambda_1CF7():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1CF7)

    def lambda_1D12():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1D12)

    def lambda_1D2D():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1D2D)

    def lambda_1D48():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1D48)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0xEE, 0x2)
    WaitChrThread(0xEE, 0x3)
    WaitChrThread(0xEF, 0x3)
    Battle(0x2AC, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_3_249 end

    def Function_4_1D7F(): pass

    label("Function_4_1D7F")

    PlayEffect(0x1, 0xFF, 0xFF, -100, -900, 18500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_4_1D7F end

    def Function_5_1DCE(): pass

    label("Function_5_1DCE")

    PlayEffect(0x1, 0xFF, 0xFF, 1910, -900, 18500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_5_1DCE end

    def Function_6_1E1D(): pass

    label("Function_6_1E1D")

    PlayEffect(0x1, 0xFF, 0xFF, -2700, -900, 15870, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_6_1E1D end

    def Function_7_1E6C(): pass

    label("Function_7_1E6C")

    PlayEffect(0x1, 0xFF, 0xFF, 4200, -900, 16059, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_7_1E6C end

    def Function_8_1EBB(): pass

    label("Function_8_1EBB")

    PlayEffect(0x1, 0xFF, 0xFF, -110, -900, 13340, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_8_1EBB end

    def Function_9_1F0A(): pass

    label("Function_9_1F0A")

    PlayEffect(0x1, 0xFF, 0xFF, 2000, -900, 13110, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_9_1F0A end

    def Function_10_1F59(): pass

    label("Function_10_1F59")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x0)
    Sleep(1000)
    OP_1D(0xAD)
    SetMapFlags(0x2000000)
    OP_44(0xEE, 0x0)
    OP_44(0xEF, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x0)
    OP_44(0x13, 0x0)
    OP_44(0x14, 0x0)
    OP_44(0x15, 0x0)
    OP_44(0x16, 0x0)
    OP_44(0x17, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 1600, -1000, 15930, 180)
    SetChrChipByIndex(0x10, 8)
    SetChrSubChip(0x10, 3)
    SetChrFlags(0x10, 0x800)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -30, -1000, 15930, 180)
    SetChrChipByIndex(0x11, 9)
    SetChrSubChip(0x11, 3)
    SetChrFlags(0x11, 0x800)
    OP_43(0x10, 0x3, 0x0, 0xC)
    OP_43(0x11, 0x3, 0x0, 0xC)
    LoadEffect(0x0, "map\\mp259_02.eff")
    LoadEffect(0x1, "map\\mp256_00.eff")
    OP_22(0x146, 0x1, 0x3C)
    PlayEffect(0x0, 0x0, 0x10, 50, 600, 100, 0, 0, 0, 2200, 2400, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x0, 0x2, 0x11, 0, 600, 100, 0, 0, 0, 2200, 2400, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_226D")
    SetChrPos(0x109, -110, -1000, 11150, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2163")
    SetChrPos(0x102, 1770, -1000, 12840, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2130")
    SetChrPos(0x10B, 250, -1000, 12840, 0)
    SetChrPos(0xF1, 1860, -1000, 11140, 0)
    Jump("loc_2160")

    label("loc_2130")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2160")
    SetChrPos(0x10B, 250, -1000, 12840, 0)
    SetChrPos(0xF0, 1860, -1000, 11140, 0)

    label("loc_2160")

    Jump("loc_226A")

    label("loc_2163")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21E8")
    SetChrPos(0x102, 1770, -1000, 12840, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21B5")
    SetChrPos(0x10B, 250, -1000, 12840, 0)
    SetChrPos(0xF1, 1860, -1000, 11140, 0)
    Jump("loc_21E5")

    label("loc_21B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21E5")
    SetChrPos(0x10B, 250, -1000, 12840, 0)
    SetChrPos(0xEF, 1860, -1000, 11140, 0)

    label("loc_21E5")

    Jump("loc_226A")

    label("loc_21E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_226A")
    SetChrPos(0x102, 1770, -1000, 12840, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_223A")
    SetChrPos(0x10B, 250, -1000, 12840, 0)
    SetChrPos(0xF0, 1860, -1000, 11140, 0)
    Jump("loc_226A")

    label("loc_223A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_226A")
    SetChrPos(0x10B, 250, -1000, 12840, 0)
    SetChrPos(0xEF, 1860, -1000, 11140, 0)

    label("loc_226A")

    Jump("loc_2347")

    label("loc_226D")

    SetChrPos(0x109, 1770, -1000, 12840, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22C2")
    SetChrPos(0x102, 250, -1000, 12840, 0)
    SetChrPos(0xF0, -110, -1000, 11150, 0)
    SetChrPos(0xF1, 1860, -1000, 11140, 0)
    Jump("loc_2347")

    label("loc_22C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2306")
    SetChrPos(0x102, 250, -1000, 12840, 0)
    SetChrPos(0xEF, -110, -1000, 11150, 0)
    SetChrPos(0xF1, 1860, -1000, 11140, 0)
    Jump("loc_2347")

    label("loc_2306")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2347")
    SetChrPos(0x102, 250, -1000, 12840, 0)
    SetChrPos(0xEF, -110, -1000, 11150, 0)
    SetChrPos(0xF0, 1860, -1000, 11140, 0)

    label("loc_2347")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(2640, -1000, 15290, 0)
    OP_67(0, 5220, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(45000, 0)
    OP_6E(229, 0)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #44
        0x11,
        (
            "#203F#5P#40W呼……\x01",
            "实在是棘手啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        (
            "#490F#5P#40W嘿嘿……\x01",
            "这下也放心了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_244E")

    ChrTalk(    #46
        0x10B,
        "#418F#6P吉尔哥，多伦哥……\x02",
    )

    CloseMessageWindow()

    label("loc_244E")


    ChrTalk(    #47
        0x102,
        "#1503F#12P你们……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x10,
        (
            "#198F#5P#40W唉，不用说你们也知道，\x01",
            "我们只是先锋而已……\x02\x03",

            "#490F后面等着你们的可都是些怪物，\x01",
            "要当心啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x11,
        (
            "#200F#5P#40W还有……\x01",
            "看起来只有我们\x01",
            "能够存留在这个世界里……\x02\x03",

            "#202F应该多少能给你们点帮助，\x01",
            "那就请多关照啦……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_2575():
        OP_6B(4500, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_2575)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x10, -100, -930, 0, 0, 0, 0, 2100, 2100, 2100, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x1, 0x3, 0x11, -100, -930, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_23(0x146)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    OP_44(0x10, 0x3)
    OP_44(0x11, 0x3)

    def lambda_2618():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2618)

    def lambda_262A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_262A)
    Sleep(800)
    Fade(1000)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    OP_0D()
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/M5408   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_1F59 end

    def Function_11_2674(): pass

    label("Function_11_2674")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_282E")
    SetChrPos(0x109, 310, -1000, 11150, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2724")
    SetChrPos(0x102, 1770, -1000, 12840, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26F1")
    SetChrPos(0x10B, 250, -1000, 12840, 0)
    SetChrPos(0xF1, 1660, -1000, 11140, 0)
    Jump("loc_2721")

    label("loc_26F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2721")
    SetChrPos(0x10B, 250, -1000, 12840, 0)
    SetChrPos(0xF0, 1660, -1000, 11140, 0)

    label("loc_2721")

    Jump("loc_282B")

    label("loc_2724")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27A9")
    SetChrPos(0x102, 1770, -1000, 12840, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2776")
    SetChrPos(0x10B, 250, -1000, 12840, 0)
    SetChrPos(0xF1, 1660, -1000, 11140, 0)
    Jump("loc_27A6")

    label("loc_2776")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27A6")
    SetChrPos(0x10B, 250, -1000, 12840, 0)
    SetChrPos(0xEF, 1660, -1000, 11140, 0)

    label("loc_27A6")

    Jump("loc_282B")

    label("loc_27A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_282B")
    SetChrPos(0x102, 1770, -1000, 12840, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27FB")
    SetChrPos(0x10B, 250, -1000, 12840, 0)
    SetChrPos(0xF0, 1660, -1000, 11140, 0)
    Jump("loc_282B")

    label("loc_27FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_282B")
    SetChrPos(0x10B, 250, -1000, 12840, 0)
    SetChrPos(0xEF, 1660, -1000, 11140, 0)

    label("loc_282B")

    Jump("loc_2908")

    label("loc_282E")

    SetChrPos(0x109, 1770, -1000, 12840, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2883")
    SetChrPos(0x102, 250, -1000, 12840, 0)
    SetChrPos(0xF0, -110, -1000, 11150, 0)
    SetChrPos(0xF1, 1860, -1000, 11140, 0)
    Jump("loc_2908")

    label("loc_2883")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28C7")
    SetChrPos(0x102, 250, -1000, 12840, 0)
    SetChrPos(0xEF, -110, -1000, 11150, 0)
    SetChrPos(0xF1, 1860, -1000, 11140, 0)
    Jump("loc_2908")

    label("loc_28C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2908")
    SetChrPos(0x102, 250, -1000, 12840, 0)
    SetChrPos(0xEF, -110, -1000, 11150, 0)
    SetChrPos(0xF0, 1860, -1000, 11140, 0)

    label("loc_2908")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(2310, -1000, 13300, 0)
    OP_67(0, 5950, -10000, 0)
    OP_6B(3260, 0)
    OP_6C(45000, 0)
    OP_6E(250, 0)
    Sleep(500)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E74")

    ChrTalk(    #50
        0x10B,
        (
            "#417F#5P………………………………\x02\x03",

            "#415F啊哈哈……\x01",
            "真不敢相信是假货啊。\x02\x03",

            "无论哪点\x01",
            "都和大哥他们一模一样……\x02",
        )
    )

    Jump("loc_2A1E")

    label("loc_2A1E")

    CloseMessageWindow()
    OP_8C(0x102, 270, 400)
    Sleep(300)

    ChrTalk(    #51
        0x102,
        "#1503F#11P乔丝特……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10B, 90, 400)
    Sleep(300)

    ChrTalk(    #52
        0x10B,
        (
            "#413F#6P嗯……\x01",
            "不过这样我反而也放心了。\x02\x03",

            "#210F看来真正的大哥他们，\x01",
            "并没有被卷入这个世界里。\x02\x03",

            "#211F好，\x01",
            "要加倍努力回到原来的世界！\x02",
        )
    )

    Jump("loc_2AF9")

    label("loc_2AF9")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B36")

    ChrTalk(    #53
        0x101,
        "#1006F#12P啊啊，就是这股气势！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DCF")

    label("loc_2B36")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B70")

    ChrTalk(    #54
        0x10F,
        "#1442F#12P……就是这股气势。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DCF")

    label("loc_2B70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BA9")

    ChrTalk(    #55
        0x107,
        "#560F#12P就、就是这股气势。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DCF")

    label("loc_2BA9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BE4")

    ChrTalk(    #56
        0x10A,
        "#816F#12P嗯嗯，就是这股气势！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DCF")

    label("loc_2BE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C23")

    ChrTalk(    #57
        0x105,
        (
            "#1168F#12P呵呵……\x01",
            "就是这股气势。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DCF")

    label("loc_2C23")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C5B")

    ChrTalk(    #58
        0x103,
        "#1521F哈哈，就是这股气势。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DCF")

    label("loc_2C5B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C94")

    ChrTalk(    #59
        0x106,
        "#051F呵呵……就是这股气势。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DCF")

    label("loc_2C94")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CCB")

    ChrTalk(    #60
        0x108,
        "#071F哈哈，就是这股气势。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DCF")

    label("loc_2CCB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D02")

    ChrTalk(    #61
        0x10E,
        "#171F呵呵，就是这股气势。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DCF")

    label("loc_2D02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D36")

    ChrTalk(    #62
        0x104,
        "#1541F嗯，就是这股气势\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DCF")

    label("loc_2D36")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D61")

    ChrTalk(    #63
        0x10D,
        "#275F呵呵……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DCF")

    label("loc_2D61")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D98")

    ChrTalk(    #64
        0x10C,
        "#111F呵呵，就是这股气势。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DCF")

    label("loc_2D98")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DCF")

    ChrTalk(    #65
        0x110,
        (
            "#261F呵呵。\x01",
            "姐姐好有气势哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DCF")


    ChrTalk(    #66
        0x109,
        (
            "#1075F#6P……看起来，\x01",
            "方舟前面的地区\x01",
            "好像可以通行了。\x02\x03",

            "#1078F鼓足干劲继续挑战吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2E3A():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2E3A)
    Sleep(100)
    OP_8C(0x10B, 180, 400)
    Sleep(300)

    ChrTalk(    #67
        0x102,
        "#1500F#5P嗯……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3454")

    label("loc_2E74")


    ChrTalk(    #68
        0x102,
        (
            "#1503F#6P…………………………………\x02\x03",

            "#1513F哈哈……\x01",
            "真像那些人的风格啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3114")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F7F")

    ChrTalk(    #69
        0x110,
        (
            "#260F#12P呼，\x01",
            "真是一群老好人啊。\x02\x03",

            "#261F可以和艾丝蒂尔平分秋色了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x10F,
        "#1806F#12P呵呵……没错。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3090")

    label("loc_2F7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3009")

    ChrTalk(    #71
        0x110,
        (
            "#260F#12P呼，\x01",
            "真是一群老好人啊。\x02\x03",

            "#261F可以和艾丝蒂尔平分秋色了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x109,
        "#1840F#5P哈哈，就是嘛。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3090")

    label("loc_3009")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3090")

    ChrTalk(    #73
        0x10F,
        (
            "#1447F#12P……真是些\x01",
            "老好人啊。\x02\x03",

            "#1806F可以和艾丝蒂尔平分秋色了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x109,
        "#1840F#5P哈哈，就是嘛。\x02",
    )

    CloseMessageWindow()

    label("loc_3090")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3111")

    ChrTalk(    #75
        0x101,
        (
            "#1016F#12P我、我说……\x02\x03",

            "#1006F不过，\x01",
            "这样乔丝特也能稍微安心点吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x102,
        "#1513F#6P……嗯。\x02",
    )

    CloseMessageWindow()

    label("loc_3111")

    Jump("loc_331B")

    label("loc_3114")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31B3")

    ChrTalk(    #77
        0x101,
        (
            "#1016F#12P真是的……\x01",
            "一点都没变，还是一群老好人。\x02\x03",

            "#1006F不过，\x01",
            "这样乔丝特也能稍微安心点吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x102,
        "#1513F#6P……嗯。\x02",
    )

    CloseMessageWindow()
    Jump("loc_331B")

    label("loc_31B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31FE")

    ChrTalk(    #79
        0x104,
        (
            "#1541F#12P呵呵，\x01",
            "老好人的性格看来还是没变呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_331B")

    label("loc_31FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3249")

    ChrTalk(    #80
        0x103,
        (
            "#1521F#12P真是的……\x01",
            "老好人的性格还是没变啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_331B")

    label("loc_3249")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3286")

    ChrTalk(    #81
        0x106,
        "#051F#12P哼……真是一帮老好人。\x02",
    )

    CloseMessageWindow()
    Jump("loc_331B")

    label("loc_3286")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32D2")

    ChrTalk(    #82
        0x108,
        (
            "#070F#12P呵呵，一点也没变，\x01",
            "老好人还是老好人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_331B")

    label("loc_32D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_331B")

    ChrTalk(    #83
        0x10C,
        (
            "#119F#12P呵呵，还是老样子，\x01",
            "老好人就是老好人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_331B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3360")

    ChrTalk(    #84
        0x107,
        (
            "#066F#12P呵呵呵……\x01",
            "都是一群很善良的人呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3360")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33A7")

    ChrTalk(    #85
        0x10D,
        (
            "#278F#12P呵呵……\x01",
            "这些人完全称不上是坏人啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33A7")


    def lambda_33AD():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_33AD)
    Sleep(100)
    OP_8C(0x109, 270, 400)
    Sleep(300)

    ChrTalk(    #86
        0x102,
        (
            "#1500F#6P……看起来，\x01",
            "方舟前面的地区\x01",
            "好像可以通行了。\x02\x03",

            "做好万全准备后前去挑战吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x109,
        "#1078F#11P啊啊……没错……！\x02",
    )

    CloseMessageWindow()

    label("loc_3454")

    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x2B27)
    OP_28(0x3A, 0x1, 0x40)
    OP_28(0x3A, 0x1, 0x80)
    OP_6D(910, -1000, 10500, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 910, -1000, 10500, 180)
    SetChrPos(0x1, 910, -1000, 10500, 180)
    SetChrPos(0x2, 910, -1000, 10500, 180)
    SetChrPos(0x3, 910, -1000, 10500, 180)
    OP_21()
    Sleep(500)
    FadeToBright(1000, 0)
    OP_1D(0xEA)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x2000000)
    EventEnd(0x0)
    Return()

    # Function_11_2674 end

    def Function_12_3516(): pass

    label("Function_12_3516")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3537")
    Sleep(100)
    Jump("loc_35B2")

    label("loc_3537")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_354C")
    Sleep(200)
    Jump("loc_35B2")

    label("loc_354C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3561")
    Sleep(300)
    Jump("loc_35B2")

    label("loc_3561")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3576")
    Sleep(400)
    Jump("loc_35B2")

    label("loc_3576")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_358B")
    Sleep(500)
    Jump("loc_35B2")

    label("loc_358B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35A0")
    Sleep(600)
    Jump("loc_35B2")

    label("loc_35A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35B2")
    Sleep(700)

    label("loc_35B2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_35D4")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x5DC)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
    Jump("loc_35B2")

    label("loc_35D4")

    Return()

    # Function_12_3516 end

    SaveToFile()

Try(main)
