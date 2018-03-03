from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1101   ._SN',
        MapName             = 'Bose',
        Location            = 'T1101.x',
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Mayor Maybelle',                       # 9
        'Lila',                                 # 10
        'Jacob',                                # 11
        'Harry',                                # 12
        'Mina',                                 # 13
        'Orvid',                                # 14
        'Elegia',                               # 15
        'Letta',                                # 16
        'Fannie',                               # 17
        'Sister Rosa',                          # 18
        'Lenard',                               # 19
        'Anelace',                              # 20
        'Target Camera',                        # 21
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
        'ED6_DT07/CH02360 ._CH',             # 00
        'ED6_DT07/CH02370 ._CH',             # 01
        'ED6_DT07/CH01000 ._CH',             # 02
        'ED6_DT07/CH01160 ._CH',             # 03
        'ED6_DT07/CH01170 ._CH',             # 04
        'ED6_DT07/CH01120 ._CH',             # 05
        'ED6_DT07/CH01150 ._CH',             # 06
        'ED6_DT07/CH01040 ._CH',             # 07
        'ED6_DT07/CH01050 ._CH',             # 08
        'ED6_DT07/CH01410 ._CH',             # 09
        'ED6_DT07/CH01270 ._CH',             # 0A
        'ED6_DT27/CH03090 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT07/CH02360P._CP',             # 00
        'ED6_DT07/CH02370P._CP',             # 01
        'ED6_DT07/CH01000P._CP',             # 02
        'ED6_DT07/CH01160P._CP',             # 03
        'ED6_DT07/CH01170P._CP',             # 04
        'ED6_DT07/CH01120P._CP',             # 05
        'ED6_DT07/CH01150P._CP',             # 06
        'ED6_DT07/CH01040P._CP',             # 07
        'ED6_DT07/CH01050P._CP',             # 08
        'ED6_DT07/CH01410P._CP',             # 09
        'ED6_DT07/CH01270P._CP',             # 0A
        'ED6_DT27/CH03090P._CP',             # 0B
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
        X                   = 48310,
        Z                   = 0,
        Y                   = 46460,
        Direction           = 262,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 35880,
        Z                   = 0,
        Y                   = 53880,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 35880,
        Z                   = 0,
        Y                   = 52760,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 49430,
        Z                   = 0,
        Y                   = 47820,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 63060,
        Z                   = 0,
        Y                   = 49000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 68240,
        Z                   = 0,
        Y                   = 53360,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 68240,
        Z                   = 0,
        Y                   = 51940,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 26500,
        Z                   = 0,
        Y                   = 12600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_2AA",          # 00, 0
        "Function_1_329",          # 01, 1
        "Function_2_32A",          # 02, 2
        "Function_3_4A7",          # 03, 3
        "Function_4_5A4",          # 04, 4
        "Function_5_6A1",          # 05, 5
        "Function_6_145C",         # 06, 6
        "Function_7_1471",         # 07, 7
        "Function_8_149A",         # 08, 8
        "Function_9_14D8",         # 09, 9
        "Function_10_1516",        # 0A, 10
        "Function_11_157A",        # 0B, 11
        "Function_12_15DA",        # 0C, 12
        "Function_13_1638",        # 0D, 13
        "Function_14_179A",        # 0E, 14
        "Function_15_18D5",        # 0F, 15
        "Function_16_2D9C",        # 10, 16
        "Function_17_332B",        # 11, 17
    )


    def Function_0_2AA(): pass

    label("Function_0_2AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CB")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_2CB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_328")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_2ED")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 15)
    Jump("loc_328")

    label("loc_2ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_30C")
    OP_A3(0x2505)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 16)
    Jump("loc_328")

    label("loc_30C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_328")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(0, 17)

    label("loc_328")

    Return()

    # Function_0_2AA end

    def Function_1_329(): pass

    label("Function_1_329")

    Return()

    # Function_1_329 end

    def Function_2_32A(): pass

    label("Function_2_32A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34F")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_491")

    label("loc_34F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_368")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_491")

    label("loc_368")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_381")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_491")

    label("loc_381")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39A")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_491")

    label("loc_39A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B3")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_491")

    label("loc_3B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CC")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_491")

    label("loc_3CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E5")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_491")

    label("loc_3E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FE")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_491")

    label("loc_3FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_417")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_491")

    label("loc_417")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_430")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_491")

    label("loc_430")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_449")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_491")

    label("loc_449")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_462")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_491")

    label("loc_462")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47B")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_491")

    label("loc_47B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_491")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_491")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A6")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_491")

    label("loc_4A6")

    Return()

    # Function_2_32A end

    def Function_3_4A7(): pass

    label("Function_3_4A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A3")
    OP_8E(0xFE, 0xF654, 0x0, 0x119F4, 0x9C4, 0x0)
    OP_8E(0xFE, 0xF2A8, 0x0, 0x12214, 0x9C4, 0x0)
    OP_8E(0xFE, 0xEF74, 0x0, 0x12426, 0x9C4, 0x0)
    OP_8E(0xFE, 0x8A16, 0x0, 0x12426, 0x9C4, 0x0)
    OP_8E(0xFE, 0x839A, 0x0, 0x120A2, 0x9C4, 0x0)
    OP_8E(0xFE, 0x8048, 0x0, 0x11E36, 0x9C4, 0x0)
    OP_8E(0xFE, 0x8048, 0x0, 0xBC66, 0x9C4, 0x0)
    OP_8E(0xFE, 0x8264, 0x0, 0xB414, 0x9C4, 0x0)
    OP_8E(0xFE, 0x85E8, 0x0, 0xAFE6, 0x9C4, 0x0)
    OP_8E(0xFE, 0xEB96, 0x0, 0xAFE6, 0x9C4, 0x0)
    OP_8E(0xFE, 0xF122, 0x0, 0xB1C6, 0x9C4, 0x0)
    OP_8E(0xFE, 0xF654, 0x0, 0xB874, 0x9C4, 0x0)
    Jump("Function_3_4A7")

    label("loc_5A3")

    Return()

    # Function_3_4A7 end

    def Function_4_5A4(): pass

    label("Function_4_5A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A0")
    OP_8E(0xFE, 0x8E44, 0x0, 0xB57C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x88F4, 0x0, 0xB770, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8750, 0x0, 0xB9DC, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8750, 0x0, 0x118D2, 0x7D0, 0x0)
    OP_8E(0xFE, 0x88C2, 0x0, 0x11D00, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8B1A, 0x0, 0x11E4A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xEA06, 0x0, 0x11E4A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xEE34, 0x0, 0x11CBA, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF046, 0x0, 0x11A62, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF046, 0x0, 0xBB44, 0x7D0, 0x0)
    OP_8E(0xFE, 0xED62, 0x0, 0xB6EE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xEB82, 0x0, 0xB57C, 0x7D0, 0x0)
    Jump("Function_4_5A4")

    label("loc_6A0")

    Return()

    # Function_4_5A4 end

    def Function_5_6A1(): pass

    label("Function_5_6A1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(49340, 0, 59250, 0)
    OP_67(0, 19070, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(171000, 0)
    OP_6E(683, 0)
    OP_11(0xA4, 0xB7, 0xFF, 0x61A8, 0x29810, 0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    Sleep(500)
    StopSound(0x9470, 0x14C08, 0x3A98)

    def lambda_749():
        OP_6D(46310, 0, 55980, 3000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_749)

    def lambda_761():
        OP_67(0, 5680, -10000, 15000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_761)

    def lambda_779():
        OP_6B(2530, 15000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_779)

    def lambda_789():
        OP_6C(90000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_789)

    def lambda_799():
        OP_6E(380, 15000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_799)
    OP_1D(0xB)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x0, 0x0)

    def lambda_7BA():
        OP_6D(74510, 500, 44650, 9000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_7BA)
    WaitChrThread(0x0, 0x0)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x16, 0x80)
    OP_4A(0x12, 255)
    OP_4A(0x16, 255)
    Sleep(3000)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    OP_73(0x0)

    def lambda_805():
        OP_6D(70000, 0, 45120, 4500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_805)
    OP_43(0x10, 0x0, 0x0, 0xB)
    OP_43(0x19, 0x0, 0x0, 0xC)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x19, 0x0)
    WaitChrThread(0x0, 0x0)

    ChrTalk(    #0
        0x19,
        (
            "#5PThank you very much for coming today.\x02\x03",

            "I would like it very much if you would be able to\x01",
            "start coming to pray like this more often, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        (
            "#610F*sigh* I'm afraid it looks as though I'm not\x01",
            "going to have much choice in that matter.\x02\x03",

            "If I show any signs of skipping mass lately, \x01",
            "Lila gives me a serious lecturing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x19,
        (
            "#5PHeehee. You're rather fortunate to have someone\x01",
            "like that by your side, if you ask me.\x02\x03",

            "The ideal partner is someone who isn't afraid to\x01",
            "criticize your choices, rather than someone who\x01",
            "just blindly supports them.\x02\x03",

            "I'm so glad that she's well now, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        (
            "#610FAs am I...\x02\x03",

            "The market's back to normal, that flying city has\x01",
            "gone...\x02\x03",

            "Everything is basically back to normal here now,\x01",
            "and what a relief that is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x19,
        (
            "#5PIndeed. Let us both offer our prayers to the\x01",
            "Goddess, that this peace might continue.\x02\x03",

            "...And on that note, I will be looking forward to\x01",
            "seeing you again here soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        (
            "#610FIndeed. Please give my regards to Father Holstein,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x19,
        "#5PI shall. Goodbye for today, then.\x02",
    )

    CloseMessageWindow()
    OP_43(0x19, 0x0, 0x0, 0xA)
    WaitChrThread(0x19, 0x0)
    OP_6F(0x0, 59)
    OP_70(0x0, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x0)
    Sleep(300)
    OP_8C(0x10, 270, 400)
    Sleep(300)

    ChrTalk(    #7
        0x10,
        (
            "#610F#5PRight...\x02\x03",

            "Next, I should make my way over to the market.\x01",
            "Inspecting that is next in my schedule.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_CE7():
        OP_6D(67100, 0, 45120, 1500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_CE7)
    OP_8E(0x10, 0xFC39, 0x0, 0xAF6E, 0x7D0, 0x0)
    WaitChrThread(0x10, 0x0)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(600)
    OP_8C(0x10, 0, 400)
    WaitChrThread(0x0, 0x0)

    ChrTalk(    #8
        0x10,
        "#610F#5PWait, isn't that...?\x02",
    )

    CloseMessageWindow()

    def lambda_D62():
        OP_6D(62800, 0, 61880, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_D62)

    def lambda_D7A():
        OP_67(0, 4950, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_D7A)

    def lambda_D92():
        OP_6B(2360, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_D92)

    def lambda_DA2():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_DA2)

    def lambda_DB2():
        OP_6E(392, 4000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_DB2)
    Sleep(2000)
    OP_43(0x11, 0x0, 0x0, 0x9)
    OP_43(0x1A, 0x0, 0x0, 0x8)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x1A, 0x0)
    WaitChrThread(0x0, 0x0)
    Sleep(300)
    SetChrPos(0x10, 69740, 0, 46480, 0)

    NpcTalk(    #9
        0x1A,
        "Pleasant Man",
        "#5PThanks so much. I had a whole lot of fun today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x11,
        "#620FAs did I.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #11
        0x1A,
        "Pleasant Man",
        (
            "#5PGet in touch again soon, okay?\x02\x03",

            "My little sister's been eagerly looking forward\x01",
            "to the big day, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x11,
        (
            "#620FOf course.\x02\x03",

            "And with that, I'm afraid I must get going.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #13
        0x1A,
        "Pleasant Man",
        (
            "#5POh, yeah. It's about time for mass to end,\x01",
            "huh?\x02\x03",

            "Later!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x11,
        "#620FIndeed.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_8C(0x1A, 0, 400)
    Sleep(200)

    def lambda_F7F():
        OP_8E(0xFE, 0xF51E, 0x0, 0x11332, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_F7F)
    Sleep(3000)
    Fade(500)
    OP_6D(70600, 0, 47820, 0)
    OP_67(0, 8550, -10000, 0)
    OP_6B(1880, 0)
    OP_6C(45000, 0)
    OP_6E(392, 0)
    OP_0D()
    Sleep(300)
    OP_44(0x1A, 0x0)
    OP_44(0x11, 0x0)
    SetChrFlags(0x1A, 0x80)

    ChrTalk(    #15
        0x10,
        (
            "#610F#5PD-Did I just witness what I think I did...?\x02\x03",

            "...\x02\x03",

            "Still, I suppose it shouldn't come as much of a\x01",
            "surprise, given her age.\x02\x03",

            "While she might be kind of cold towards people,\x01",
            "she's a wonderful girl, and an attractive one,\x01",
            "too.\x02\x03",

            "If anything, I'm surprised it's taken her this\x01",
            "long to find someone.\x02\x03",

            "I can't deny that I do feel a little lonely at\x01",
            "the thought, but she's going to want my support.\x01",
            "It wouldn't be right for me not to give her it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11B8():
        OP_6D(68530, 0, 47650, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_11B8)

    def lambda_11D0():
        OP_67(0, 8770, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_11D0)

    def lambda_11E8():
        OP_6B(1780, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_11E8)
    SetChrPos(0x11, 63970, 0, 53590, 180)

    def lambda_1209():
        OP_8E(0xFE, 0x10040, 0x0, 0xB61C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1209)
    WaitChrThread(0x11, 0x1)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(600)
    OP_8C(0x11, 90, 400)
    Sleep(300)

    ChrTalk(    #16
        0x11,
        (
            "#620F#6PUmm...\x02\x03",

            "Might I ask exactly what you are doing?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_12B7():
        OP_8F(0xFE, 0x1108A, 0x0, 0xB432, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_12B7)
    OP_8C(0x10, 270, 500)
    WaitChrThread(0x10, 0x0)
    Sleep(200)

    ChrTalk(    #17
        0x10,
        (
            "#610FO-Oh... It's you, Lila...\x02\x03",

            "H-How long have you been there?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #18
        0x11,
        (
            "#620F...\x02\x03",

            "You appear to be rather tired.\x02\x03",

            "This is why I keep telling you that you need to\x01",
            "stop overexerting yourself...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        (
            "#610FOh, no, I'm not, I assure you.\x02\x03",

            "Well, shall we be going to the market?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x11,
        "#620FWell, if you say so...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_43(0x10, 0x0, 0x0, 0x7)

    def lambda_1428():

        label("loc_1428")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1428")

    QueueWorkItem2(0x11, 0, lambda_1428)
    Sleep(3000)
    OP_43(0x11, 0x0, 0x0, 0x6)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T1111   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_6A1 end

    def Function_6_145C(): pass

    label("Function_6_145C")

    OP_8E(0xFE, 0xF730, 0x0, 0xE74A, 0x7D0, 0x0)
    Return()

    # Function_6_145C end

    def Function_7_1471(): pass

    label("Function_7_1471")

    OP_8F(0xFE, 0xFDA2, 0x0, 0xBAF4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF730, 0x0, 0xE74A, 0x7D0, 0x0)
    Return()

    # Function_7_1471 end

    def Function_8_149A(): pass

    label("Function_8_149A")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 58570, 0, 60450, 90)

    def lambda_14B6():
        OP_8E(0xFE, 0xF51E, 0x0, 0xEC22, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14B6)
    WaitChrThread(0xFE, 0x1)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_8_149A end

    def Function_9_14D8(): pass

    label("Function_9_14D8")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 58390, 0, 58930, 90)

    def lambda_14F4():
        OP_8E(0xFE, 0xF51E, 0x0, 0xE54C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14F4)
    WaitChrThread(0xFE, 0x1)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_9_14D8 end

    def Function_10_1516(): pass

    label("Function_10_1516")

    OP_8C(0xFE, 90, 400)

    def lambda_1523():
        OP_8E(0xFE, 0x11D5A, 0x1F4, 0xADDE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1523)
    WaitChrThread(0xFE, 0x2)

    def lambda_1543():
        OP_8E(0xFE, 0x120E8, 0x1F4, 0xADE8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1543)

    def lambda_155E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_155E)
    WaitChrThread(0xFE, 0x2)
    WaitChrThread(0xFE, 0x1)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_10_1516 end

    def Function_11_157A(): pass

    label("Function_11_157A")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 74570, 500, 44500, 270)

    def lambda_15A1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_15A1)

    def lambda_15B3():
        OP_8E(0xFE, 0x10658, 0x0, 0xAF6E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_15B3)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_11_157A end

    def Function_12_15DA(): pass

    label("Function_12_15DA")

    Sleep(900)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 74570, 500, 44500, 270)

    def lambda_1606():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1606)

    def lambda_1618():
        OP_8E(0xFE, 0x110A8, 0x0, 0xAFAA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1618)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_12_15DA end

    def Function_13_1638(): pass

    label("Function_13_1638")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(22300, 0, 55980, 0)
    OP_67(0, 9330, -10000, 0)
    OP_6B(2790, 0)
    OP_6C(212000, 0)
    OP_6E(405, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #21
        "\x07\x05Several days later...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)

    def lambda_16F4():
        OP_6D(19230, 0, 57650, 6000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_16F4)

    def lambda_170C():
        OP_67(0, 7970, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_170C)

    def lambda_1724():
        OP_6B(3040, 6000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1724)

    def lambda_1734():
        OP_6C(270000, 6000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_1734)

    def lambda_1744():
        OP_6E(372, 6000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1744)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x0, 0x0)

    def lambda_1763():
        OP_6B(2900, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_1763)

    def lambda_1773():
        OP_6E(355, 2000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1773)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2507)
    NewScene("ED6_DT21/T1111   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_1638 end

    def Function_14_179A(): pass

    label("Function_14_179A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    OP_6D(48000, 0, 60000, 0)
    OP_67(0, 18700, -10000, 0)
    OP_6B(2160, 0)
    OP_6C(45000, 0)
    OP_6E(746, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_C8(0x200, 0x46, "C_PLAC15._CH", 0x0, 0x7D0)
    FadeToBright(2000, 0)

    def lambda_1844():
        OP_6D(59000, 0, 84600, 9000)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_1844)

    def lambda_185C():
        OP_67(0, 6000, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_185C)

    def lambda_1874():
        OP_6B(2000, 9000)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_1874)

    def lambda_1884():
        OP_6E(616, 9000)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_1884)

    def lambda_1894():
        OP_6C(0, 9000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_1894)
    WaitChrThread(0x1C, 0x0)
    Sleep(500)

    def lambda_18AE():
        OP_6B(1900, 3000)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_18AE)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T1121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_179A end

    def Function_15_18D5(): pass

    label("Function_15_18D5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    OP_6D(49340, 0, 59250, 0)
    OP_67(0, 19070, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(171000, 0)
    OP_6E(683, 0)
    OP_11(0xA4, 0xB7, 0xFF, 0x61A8, 0x29810, 0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    StopSound(0x9470, 0x14C08, 0x3A98)

    def lambda_197E():
        OP_6D(46310, 0, 55980, 3000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_197E)

    def lambda_1996():
        OP_67(0, 5680, -10000, 15000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1996)

    def lambda_19AE():
        OP_6B(2530, 15000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_19AE)

    def lambda_19BE():
        OP_6C(90000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_19BE)

    def lambda_19CE():
        OP_6E(380, 15000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_19CE)
    OP_C8(0x200, 0x46, "C_PLAC15._CH", 0x0, 0x7D0)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x0, 0x0)

    def lambda_1A02():
        OP_6D(74510, 500, 44650, 9000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_1A02)
    WaitChrThread(0x0, 0x0)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x16, 0x80)
    OP_4A(0x12, 255)
    OP_4A(0x16, 255)
    Sleep(3000)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    OP_73(0x0)

    def lambda_1A4D():
        OP_6D(70000, 0, 45120, 4500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_1A4D)
    OP_43(0x10, 0x0, 0x0, 0xB)
    OP_43(0x19, 0x0, 0x0, 0xC)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x19, 0x0)
    WaitChrThread(0x0, 0x0)

    ChrTalk(    #22
        0x19,
        "#5PThank you very much for coming today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x19,
        (
            "I'd love it if you would be able to start coming\x01",
            "to pray like this more often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        (
            "#615F#6P*sigh* I'm afraid it looks as though I won't\x01",
            "have a choice in that matter.\x02\x03",

            "#610FIf I show any signs of skipping mass lately, \x01",
            "Lila gives me a stern lecturing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x19,
        (
            "#5PYou're rather fortunate to have someone like her\x01",
            "by your side, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x19,
        (
            "#5PNothing is more valuable to a person than someone \x01",
            "who will chide them when they seem to be straying \x01",
            "from the right path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        (
            "#610F#6POh, I couldn't agree more.\x02\x03",

            "#618FI do wish she should go a little easier on me\x01",
            "than she currently does, however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x19,
        (
            "#5PLook at it this way: the fact that she doesn't\x01",
            "shows just how important you are to her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x19,
        (
            "#5PFor one thing, I hear you've been exceptionally\x01",
            "busy with work these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x19,
        (
            "#5PI wouldn't be surprised if she hoped to make\x01",
            "the time you spend here to be a break from all\x01",
            "of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10,
        (
            "#617F#6PAs frustrating as it is to admit, that's a scarily\x01",
            "sound assessment.\x02\x03",

            "#610FBut she can't keep me away from work forever,\x01",
            "now, can she? I think I ought to be getting back\x01",
            "to it now. So if you'll excuse me...\x02\x03",

            "Please give my regards to Father Holstein, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x19,
        "#5PHeehee. Certainly. A good day to you, then.\x02",
    )

    CloseMessageWindow()
    OP_43(0x19, 0x0, 0x0, 0xA)
    WaitChrThread(0x19, 0x0)
    OP_6F(0x0, 59)
    OP_70(0x0, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x0)
    Sleep(300)
    OP_8C(0x10, 270, 400)
    Sleep(300)

    ChrTalk(    #33
        0x10,
        (
            "#615F#5P*sigh* As if Lila wasn't bad enough, now I have\x01",
            "Sister Rosa saying the same things as her...\x02\x03",

            "#610FOhhh, well... Next up is inspecting the market,\x01",
            "so I should probably get to doing that...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 315, 400)
    Sleep(800)
    OP_8C(0x10, 225, 400)
    Sleep(800)
    OP_8C(0x10, 270, 400)
    Sleep(300)

    ChrTalk(    #34
        0x10,
        (
            "#615F#5PI was expecting Lila to be here to meet me by\x01",
            "now, though...\x02\x03",

            "#618FShe's been awfully cold to me lately, and I still\x01",
            "don't have a clue as to why.\x02\x03",

            "I thought she was going to pray with me today,\x01",
            "too, but then she up and decided she needed to\x01",
            "take care of shopping...\x02\x03",

            "#610FMaybe I can grill her on it later.\x02\x03",

            "For now, I should hurry and get to the market.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_21FD():
        OP_6D(67100, 0, 45120, 1500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_21FD)
    OP_8E(0x10, 0xFC39, 0x0, 0xAF6E, 0x7D0, 0x0)
    WaitChrThread(0x10, 0x0)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10, 0, 400)
    WaitChrThread(0x0, 0x0)
    Sleep(300)

    ChrTalk(    #35
        0x10,
        "#613F#11POh! Isn't that Lila...?\x02",
    )

    CloseMessageWindow()

    def lambda_2281():
        OP_6D(62800, 0, 61880, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_2281)

    def lambda_2299():
        OP_67(0, 4950, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2299)

    def lambda_22B1():
        OP_6B(2360, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_22B1)

    def lambda_22C1():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_22C1)

    def lambda_22D1():
        OP_6E(392, 4000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_22D1)
    Sleep(2000)
    OP_43(0x11, 0x0, 0x0, 0x9)
    OP_43(0x1A, 0x0, 0x0, 0x8)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x1A, 0x0)
    WaitChrThread(0x0, 0x0)
    Sleep(300)
    SetChrPos(0x10, 69740, 0, 46480, 0)

    NpcTalk(    #36
        0x1A,
        "Pleasant Man",
        "#5PThanks. I really do appreciate your help today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x11,
        "#620F#6PNot at all. I should be saying the same to you.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #38
        0x1A,
        "Pleasant Man",
        (
            "#5PAnyway, if you need anything else, just give me\x01",
            "a call.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #39
        0x1A,
        "Pleasant Man",
        (
            "#5PI can always worm my way out of whatever's on\x01",
            "my schedule to make time for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x11,
        "#620F#6PI'll certainly keep that in mind.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #41
        0x1A,
        "Pleasant Man",
        (
            "#5PPlease do! My little sister's been so excited for\x01",
            "the big day already.\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()

    NpcTalk(    #42
        0x1A,
        "Pleasant Man",
        "#5PIt'll surely be one to remember.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x11,
        (
            "#621FHeehee. Yes, I'm sure.\x02\x03",

            "For now, however, I really should be going.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #44
        0x1A,
        "Pleasant Man",
        (
            "#5POh, yeah. The mayor should be about done with\x01",
            "mass now, right?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #45
        0x1A,
        "Pleasant Man",
        "#5PUntil next time!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x11,
        "#620FFarewell for now.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_8C(0x1A, 0, 400)
    Sleep(200)

    def lambda_2604():
        OP_8E(0xFE, 0xF51E, 0x0, 0x11332, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_2604)
    Sleep(3000)
    Fade(500)
    OP_6D(70600, 0, 47820, 0)
    OP_67(0, 8550, -10000, 0)
    OP_6B(1880, 0)
    OP_6C(45000, 0)
    OP_6E(392, 0)
    OP_0D()
    OP_44(0x1A, 0x0)
    OP_44(0x11, 0x0)
    SetChrFlags(0x1A, 0x80)
    Sleep(500)

    ChrTalk(    #47
        0x10,
        "#613F#12PD-Did I just witness what I think I did...?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #48
        0x10,
        (
            "#615F#12PSo that's why she's been acting so distant\x01",
            "towards me lately...\x02\x03",

            "#618FI wish she had said something... I thought\x01",
            "we were supposed to be close...\x02\x03",

            "...\x02\x03",

            "#610FI suppose it shouldn't come as much of a surprise.\x01",
            "She's a grown woman.\x02\x03",

            "And she might seem cold towards people on the\x01",
            "outside, but she's a wonderful human being...and\x01",
            "a rather attractive one, too.\x02\x03",

            "If anything, I'm surprised it's taken her this long\x01",
            "to find someone.\x02\x03",

            "#617F...Well, it wouldn't be fair for me to get in the\x01",
            "way of her happiness.\x02\x03",

            "#611FI do feel a little lonely at the thought, but she's\x01",
            "going to want my support. It wouldn't be right\x01",
            "for me not to give her it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_295F():
        OP_6D(68530, 0, 47650, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_295F)

    def lambda_2977():
        OP_67(0, 8770, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2977)

    def lambda_298F():
        OP_6B(1780, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_298F)
    SetChrPos(0x11, 63970, 0, 53590, 180)

    def lambda_29B0():
        OP_8E(0xFE, 0x10040, 0x0, 0xB61C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_29B0)
    WaitChrThread(0x11, 0x1)
    Sleep(300)

    ChrTalk(    #49
        0x11,
        "#623F#5P*sigh* I'll have to apologize for being late.\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x11, 90, 400)
    Sleep(300)

    ChrTalk(    #50
        0x11,
        (
            "#622F#6PUmm...\x02\x03",

            "Might I ask exactly what you are doing?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_2A9E():
        OP_8F(0xFE, 0x1108A, 0x0, 0xB432, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2A9E)
    OP_8C(0x10, 270, 500)
    WaitChrThread(0x10, 0x0)
    Sleep(300)

    ChrTalk(    #51
        0x10,
        (
            "#613F#11PO-Oh... It's you, Lila...\x02\x03",

            "#617FH-How long have you been there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x11,
        (
            "#622F#6P...\x02\x03",

            "#625FYou appear to be rather tired.\x02\x03",

            "This is why I keep telling you that you need\x01",
            "to stop overexerting yourself...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10,
        (
            "#617F#11POh, no! I'm not, I assure you.\x02\x03",

            "#611FShall we head to the market?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x11,
        "#622F#6PWell, if you say so...\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_2C16():
        OP_6D(65000, 0, 55000, 7000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_2C16)

    def lambda_2C2E():
        OP_6C(33000, 7000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2C2E)
    OP_43(0x10, 0x0, 0x0, 0x7)

    def lambda_2C45():

        label("loc_2C45")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2C45")

    QueueWorkItem2(0x11, 0, lambda_2C45)
    Sleep(3000)
    OP_43(0x11, 0x0, 0x0, 0x6)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    Sleep(2000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #55
        "\x07\x00The next day...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_6D(30640, 0, 75000, 0)
    OP_67(0, 12800, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(270000, 0)
    OP_6E(502, 0)

    def lambda_2CFE():
        OP_6D(55060, 0, 75000, 6000)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_2CFE)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x1C, 0x0)

    def lambda_2D25():
        OP_6D(55060, 0, 84540, 5000)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_2D25)

    def lambda_2D3D():
        OP_67(0, 5500, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_2D3D)

    def lambda_2D55():
        OP_6B(2600, 5000)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_2D55)

    def lambda_2D65():
        OP_6E(482, 5000)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_2D65)

    def lambda_2D75():
        OP_6C(320000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_2D75)
    WaitChrThread(0x1C, 0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T1121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_18D5 end

    def Function_16_2D9C(): pass

    label("Function_16_2D9C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(36790, 0, 69390, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1B, 0x80)
    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    SetChrPos(0x13, 36000, 0, 70120, 225)
    SetChrPos(0x14, 36000, 0, 68660, 315)
    SetChrPos(0x1B, 34300, 0, 69390, 90)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #56 op#A
        "\x07\x00#15A#4STestimony 2\x18\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #57
        0x14,
        "#11PYes, I saw them.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x14,
        (
            "#11PI remember the man escorting the maid to\x01",
            "the front door of the mayor's mansion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x13,
        (
            "#5PI was surprised he didn't go inside with her,\x01",
            "honestly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x13,
        "#5PWhenever I take Mina home, I always do!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x14,
        "#11P...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14, 0, 400)
    Sleep(300)

    ChrTalk(    #62
        0x14,
        "#2P*sigh* Oh, Harry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x14,
        (
            "#2PIf you ask me, you're the one behaving improperly.\x01",
            "Not the man we're talking about.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(500)
    OP_8C(0x13, 180, 400)

    ChrTalk(    #64
        0x13,
        "#1P...I am?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x14,
        (
            "#2POrdinarily, when a gentleman escorts a lady to\x01",
            "her home, he doesn't go inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x13,
        "#1P...Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x14,
        "#2PReally.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x13,
        (
            "#1PB-But surely the fact I do that is proof that\x01",
            "we're that close, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x14,
        "#2PI wouldn't be assuming that if I were you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x14,
        (
            "#2PFor one thing, those two seemed awfully\x01",
            "close even without that, didn't they?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 1700, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #71
        0x13,
        "#1P*sniffle*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x14,
        (
            "#2PI'm not saying that it's always wrong\x01",
            "to go inside, per se.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x14,
        (
            "#2PIf that's what you want to keep doing,\x01",
            "you won't see me stopping you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x13,
        "#1PO-Okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x13,
        "#1PI-I will, then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x14,
        (
            "#2P(*sigh* Why does everything have to be\x01",
            "so much work when it comes to you...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x1B,
        "#819F#6PAhaha... Thanks for the info, anyway.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(1000)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T1110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_2D9C end

    def Function_17_332B(): pass

    label("Function_17_332B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(22300, 0, 55980, 0)
    OP_67(0, 9330, -10000, 0)
    OP_6B(2790, 0)
    OP_6C(212000, 0)
    OP_6E(405, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    Sleep(500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #78
        "\x07\x00#40WSeveral days later...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_1D(0xB)

    def lambda_33FE():
        OP_6D(19230, 0, 57650, 6000)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_33FE)

    def lambda_3416():
        OP_67(0, 7970, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_3416)

    def lambda_342E():
        OP_6B(3040, 6000)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_342E)

    def lambda_343E():
        OP_6C(270000, 6000)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_343E)

    def lambda_344E():
        OP_6E(372, 6000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_344E)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x1C, 0x0)
    Sleep(500)

    def lambda_3472():
        OP_6B(2900, 2000)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_3472)

    def lambda_3482():
        OP_6E(355, 2000)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_3482)
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearMapFlags(0x2000000)
    OP_A2(0x2507)
    NewScene("ED6_DT21/T1111   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_332B end

    SaveToFile()

Try(main)
