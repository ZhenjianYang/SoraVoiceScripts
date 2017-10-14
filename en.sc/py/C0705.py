from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C0705   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0705.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60033",
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
        'Bleublanc',                            # 9
        'Balancing Clown',                      # 10
        'Balancing Clown',                      # 11
        'Gospel',                               # 12
        'Luciola',                              # 13
        'Walter',                               # 14
        'Campanella',                           # 15
        '紅い飛行艇',                           # 16
        '紅い飛行艇影',                         # 17
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
        'ED6_DT27/CH03530 ._CH',             # 00
        'ED6_DT29/CH12160 ._CH',             # 01
        'ED6_DT27/CH04530 ._CH',             # 02
        'ED6_DT27/CH04000 ._CH',             # 03
        'ED6_DT27/CH04001 ._CH',             # 04
        'ED6_DT27/CH04010 ._CH',             # 05
        'ED6_DT27/CH04011 ._CH',             # 06
        'ED6_DT06/CH20021 ._CH',             # 07
        'ED6_DT29/CH12161 ._CH',             # 08
        'ED6_DT26/CH20273 ._CH',             # 09
        'ED6_DT27/CH03520 ._CH',             # 0A
        'ED6_DT27/CH03500 ._CH',             # 0B
        'ED6_DT27/CH03600 ._CH',             # 0C
        'ED6_DT26/CH20431 ._CH',             # 0D
        'ED6_DT27/CH03500 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT27/CH03530P._CP',             # 00
        'ED6_DT29/CH12160P._CP',             # 01
        'ED6_DT27/CH04530P._CP',             # 02
        'ED6_DT27/CH04000P._CP',             # 03
        'ED6_DT27/CH04001P._CP',             # 04
        'ED6_DT27/CH04010P._CP',             # 05
        'ED6_DT27/CH04011P._CP',             # 06
        'ED6_DT06/CH20021P._CP',             # 07
        'ED6_DT29/CH12161P._CP',             # 08
        'ED6_DT26/CH20273P._CP',             # 09
        'ED6_DT27/CH03520P._CP',             # 0A
        'ED6_DT27/CH03500P._CP',             # 0B
        'ED6_DT27/CH03600P._CP',             # 0C
        'ED6_DT26/CH20431P._CP',             # 0D
        'ED6_DT27/CH03500P._CP',             # 0E
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
        Unknown3            = 458759,
        ChipIndex           = 0x7,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x180,
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
        NpcIndex            = 0x180,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_242",          # 00, 0
        "Function_1_2B9",          # 01, 1
        "Function_2_2E0",          # 02, 2
        "Function_3_45D",          # 03, 3
        "Function_4_D1E",          # 04, 4
        "Function_5_D52",          # 05, 5
        "Function_6_D82",          # 06, 6
        "Function_7_DF0",          # 07, 7
        "Function_8_E4A",          # 08, 8
        "Function_9_1007",         # 09, 9
        "Function_10_12CE",        # 0A, 10
        "Function_11_12D7",        # 0B, 11
        "Function_12_3001",        # 0C, 12
        "Function_13_3510",        # 0D, 13
        "Function_14_3596",        # 0E, 14
    )


    def Function_0_242(): pass

    label("Function_0_242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_261")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)
    Jump("loc_2B8")

    label("loc_261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_280")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 9)
    Jump("loc_2B8")

    label("loc_280")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_29F")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_2B8")

    label("loc_29F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 5)), scpexpr(EXPR_END)), "loc_2B8")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 10)

    label("loc_2B8")

    Return()

    # Function_0_242 end

    def Function_1_2B9(): pass

    label("Function_1_2B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CA")
    OP_22(0xEB, 0x1, 0x50)

    label("loc_2CA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x454), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DF")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2DF")

    Return()

    # Function_1_2B9 end

    def Function_2_2E0(): pass

    label("Function_2_2E0")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_305")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_447")

    label("loc_305")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31E")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_447")

    label("loc_31E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_337")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_447")

    label("loc_337")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_350")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_447")

    label("loc_350")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_369")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_447")

    label("loc_369")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_382")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_447")

    label("loc_382")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39B")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_447")

    label("loc_39B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B4")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_447")

    label("loc_3B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CD")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_447")

    label("loc_3CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E6")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_447")

    label("loc_3E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FF")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_447")

    label("loc_3FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_418")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_447")

    label("loc_418")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_431")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_447")

    label("loc_431")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_447")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_447")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_45C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_447")

    label("loc_45C")

    Return()

    # Function_2_2E0 end

    def Function_3_45D(): pass

    label("Function_3_45D")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_82(0x80, 0x0)
    OP_71(0x9, 0x4)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0x4, 0x2)
    OP_7B()
    OP_6D(40, 0, 35830, 0)
    OP_67(0, 7740, -10000, 0)
    OP_6B(3700, 0)
    OP_EA(0x66, 0x1, 0x0, 0x0)
    OP_6C(45000, 0)
    OP_6E(297, 0)
    SetChrPos(0xC, 40, 0, -7480, 0)
    ClearChrFlags(0xC, 0x80)
    OP_22(0x1C3, 0x0, 0x64)
    FadeToBright(2000, 0)

    def lambda_515():
        OP_6D(40, 0, 0, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_515)
    Sleep(5000)
    OP_8E(0xC, 0x28, 0x0, 0x0, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #0
        0xC,
        (
            "#240FEsmelas Tower...\x01",
            "It's just as we heard.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_587():
        OP_6D(370, 0, 9730, 3500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_587)

    def lambda_59F():
        OP_6B(3000, 3500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_59F)

    def lambda_5AF():
        OP_67(0, 6900, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5AF)
    OP_8E(0xC, 0xA0, 0x0, 0x2026, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #1
        0xC,
        (
            "#244FOne of the four device towers\x01",
            "activated on the release of the\x01",
            "seal beneath Grancel Castle...\x02\x03",

            "A second barrier, defending the\x01",
            "Aureole from all angles...\x02\x03",

            "#241FHeehee. The professor's research\x01",
            "was spot on, it seems.\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_A1(0x10, 0x7)
    SetChrPos(0x10, -25390, 1500, 11620, 180)
    OP_72(0x7, 0x4)
    OP_22(0x79, 0x1, 0x46)
    Sleep(1000)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_24(0x79, 0x50)
    Sleep(1000)

    def lambda_707():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_707)
    OP_24(0x79, 0x55)
    Sleep(1000)

    def lambda_71E():

        label("loc_71E")

        TurnDirection(0xFE, 0x10, 100)
        OP_48()
        Jump("loc_71E")

    QueueWorkItem2(0xC, 1, lambda_71E)
    OP_24(0x79, 0x5A)

    def lambda_733():
        OP_8E(0xFE, 0x5244, 0x5DC, 0x2B7A, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_733)
    Sleep(1000)
    OP_24(0x79, 0x5F)
    Sleep(1000)
    OP_24(0x79, 0x64)
    WaitChrThread(0x10, 0x1)
    OP_44(0xC, 0x1)
    Fade(500)
    OP_6D(15450, 0, 9560, 0)
    OP_67(0, 8440, -10000, 0)
    OP_6B(4120, 0)
    OP_EA(0x66, 0x2, 0x0, 0x0)
    OP_6C(45000, 0)
    OP_6E(433, 0)
    OP_71(0x7, 0x4)
    OP_A1(0xF, 0x8)
    SetChrPos(0xF, 18810, 5000, 10000, 90)
    OP_72(0x8, 0x4)
    OP_B0(0x8, 0x14)
    OP_71(0x8, 0x20)
    OP_6F(0x8, 830)
    OP_70(0x8, 0x352)

    def lambda_7E7():
        OP_6D(19500, 250, 8310, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7E7)

    def lambda_7FF():
        OP_67(0, 6470, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7FF)
    OP_EA(0x66, 0x3, 0x0, 0x0)

    def lambda_81C():
        OP_6E(364, 10000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_81C)

    def lambda_82C():
        OP_8F(0xF, 0x5532, 0xFFFFFC18, 0x2710, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_82C)

    def lambda_847():
        OP_8C(0xF, 0, 10)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_847)
    Sleep(1000)

    def lambda_85A():
        OP_8F(0xF, 0x5532, 0xFFFFFC18, 0x2710, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_85A)

    def lambda_875():
        OP_8C(0xF, 0, 12)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_875)
    Sleep(1000)

    def lambda_888():
        OP_8F(0xF, 0x5532, 0xFFFFFC18, 0x2710, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_888)

    def lambda_8A3():
        OP_8C(0xF, 0, 15)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_8A3)
    Sleep(1000)

    def lambda_8B6():
        OP_8F(0xF, 0x5532, 0xFFFFFC18, 0x2710, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_8B6)

    def lambda_8D1():
        OP_8C(0xF, 0, 12)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_8D1)
    Sleep(1500)

    def lambda_8E4():
        OP_8C(0xF, 0, 10)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_8E4)

    def lambda_8F2():
        OP_8F(0xF, 0x5532, 0xFFFFFC18, 0x2710, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_8F2)
    WaitChrThread(0xF, 0x0)
    WaitChrThread(0xF, 0x1)
    OP_43(0xC, 0x0, 0x0, 0x5)
    OP_72(0x8, 0x20)
    OP_D8(0x8, 0x12C)
    OP_6F(0x8, 1220)
    OP_70(0x8, 0x50A)
    Sleep(1000)
    OP_22(0xFD, 0x0, 0x64)
    OP_73(0x8)
    OP_71(0x8, 0x20)
    OP_6F(0x8, 1290)
    OP_70(0x8, 0x51D)
    OP_48()
    Sleep(100)
    OP_43(0xE, 0x0, 0x0, 0x7)
    Sleep(800)
    OP_43(0xD, 0x0, 0x0, 0x6)
    Sleep(1500)
    OP_43(0xF, 0x0, 0x0, 0x4)
    WaitChrThread(0xD, 0x0)
    Sleep(200)
    OP_DC()

    ChrTalk(    #2
        0xD,
        "#252F#4PYo. Sorry to keep you waiting.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xE, 0x0)

    ChrTalk(    #3
        0xE,
        (
            "#851F#6PHaha. Hope we didn't tire you\x01",
            "too much with the delay.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 0x0)

    ChrTalk(    #4
        0xC,
        (
            "#243F#5PAh, Walter, Campanella.\x01",
            "This is a surprise.\x02\x03",

            "#240FI was sure it would be Loewe\x01",
            "who met me here.\x02\x03",

            "What turning of the wind\x01",
            "is this, I wonder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xE,
        (
            "#850F#6PLoewe is accompanying the\x01",
            "professor for the moment.\x02\x03",

            "So, as much as it may not be my place\x01",
            "as a mere observer, I came in his stead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xD,
        (
            "#250F#4PAnd, eh, I ain't got much to do at\x01",
            "this point.\x02\x03",

            "Right now I'm just killin' some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xC,
        (
            "#241F#5PHow unusual--for both of you.\x02\x03",

            "Though, interesting.\x01",
            "Loewe is accompanying the professor?\x02\x03",

            "They are performing the\x01",
            "last experiment, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xD,
        (
            "#252F#4PHeheh. Apparently.\x02\x03",

            "Our big, fancy plan is headin' into\x01",
            "the big leagues, looks like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xE,
        (
            "#853F#6PThe archaisms and jaegers are\x01",
            "almost ready.\x02\x03",

            "#850FOnce we have the beta in hand,\x01",
            "we'll all be quite busy, I suspect.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_45D end

    def Function_4_D1E(): pass

    label("Function_4_D1E")

    OP_72(0x8, 0x20)
    OP_6F(0x8, 1300)
    OP_70(0x8, 0x564)
    Sleep(500)
    OP_22(0xFD, 0x0, 0x64)
    OP_73(0x8)
    OP_71(0x8, 0x20)
    OP_6F(0x8, 800)
    OP_70(0x8, 0x384)
    Return()

    # Function_4_D1E end

    def Function_5_D52(): pass

    label("Function_5_D52")

    OP_8E(0xFE, 0x1B44, 0xFA, 0x2602, 0xBB8, 0x0)
    OP_8E(0xFE, 0x35F2, 0xFA, 0x191E, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_5_D52 end

    def Function_6_D82(): pass

    label("Function_6_D82")

    SetChrChipByIndex(0xFE, 14)
    SetChrSubChip(0xFE, 0)
    SetChrFlags(0xFE, 0x40)
    SetChrBattleFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x80)
    OP_89(0xFE, 21840, 2300, 9970, 0)
    OP_8E(0xFE, 0x5532, 0x8FC, 0x1DBA, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0x4B78, 0x938, 0x1A9A, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 270, 400)
    SetChrChipByIndex(0xFE, 13)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_6_D82 end

    def Function_7_DF0(): pass

    label("Function_7_DF0")

    SetChrFlags(0xFE, 0x40)
    SetChrBattleFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x80)
    OP_89(0xFE, 21840, 2300, 9970, 0)
    OP_8E(0xFE, 0x5532, 0x8FC, 0x1DBA, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0x497A, 0x92E, 0x1D92, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_7_DF0 end

    def Function_8_E4A(): pass

    label("Function_8_E4A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(60, 0, -2000, 0)
    OP_67(0, 8910, -10000, 0)
    OP_6B(4370, 0)
    OP_6C(21000, 0)
    OP_6E(254, 0)
    OP_22(0x1C3, 0x0, 0x64)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 4059, 3450, 6990, 315)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x1)
    OP_82(0x80, 0x0)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0x4, 0x2)
    OP_7B()
    Sleep(1000)

    def lambda_F08():
        OP_6D(520, 0, 12220, 4000)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_F08)
    OP_C8(0x200, 0x46, "C_PLAC19._CH", 0x1, 0x3E8)
    FadeToBright(1000, 0)
    WaitChrThread(0xB, 0x0)
    Sleep(1000)
    Fade(1000)
    OP_6D(1400, 0, 14000, 0)
    OP_67(0, 6630, -10000, 0)
    OP_6B(2029, 0)
    OP_6C(9000, 0)
    OP_6E(507, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #10
        0x8,
        (
            "#231F#8PThis is Bleublanc.\x02\x03",

            "The device is in place.\x01",
            "I await the beginning of the ceremony!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C3605   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_E4A end

    def Function_9_1007(): pass

    label("Function_9_1007")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(1220, 950, 14960, 0)
    OP_67(0, 8600, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(45000, 0)
    OP_6E(408, 0)
    SetChrPos(0x8, 40, 950, 12620, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 4059, 3450, 6990, 315)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x1)
    OP_82(0x80, 0x0)
    OP_72(0x0, 0x8)
    OP_72(0x1, 0x8)
    OP_72(0x2, 0x8)
    OP_72(0x3, 0x8)
    OP_72(0x4, 0x8)
    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_72(0x4, 0x20)
    OP_6F(0x0, 60)
    OP_6F(0x1, 60)
    OP_6F(0x2, 60)
    OP_6F(0x3, 60)
    OP_6F(0x4, 60)
    OP_70(0x0, 0x3C)
    OP_70(0x1, 0x3C)
    OP_70(0x2, 0x3C)
    OP_70(0x3, 0x3C)
    LoadEffect(0x1, "map\\\\mp061_00.eff")
    PlayEffect(0x1, 0xFF, 0xFF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_E8(0xD0, 0x7, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_B0(0x0, 0x50)
    OP_B0(0x1, 0x50)
    OP_B0(0x2, 0x50)
    OP_B0(0x3, 0x50)
    OP_B0(0x4, 0x50)
    OP_22(0x99, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)
    OP_73(0x1)
    OP_22(0x99, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)
    OP_73(0x2)
    OP_22(0x99, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)
    OP_73(0x3)
    OP_22(0x99, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)
    OP_73(0x4)
    OP_22(0x99, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_79(0x0, 0x1)
    OP_79(0x1, 0x1)
    OP_79(0x2, 0x1)
    OP_79(0x3, 0x1)
    OP_79(0x4, 0x1)
    OP_7B()
    Fade(1000)
    OP_11(0xA0, 0xB4, 0xFF, 0x17ED0, 0x38E28, 0x0)
    OP_6D(-32090, 30000, -26260, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
    OP_6E(300, 0)
    OP_0D()
    LoadEffect(0x0, "map\\mp049_03.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -32090, 30000, -26260, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    Sleep(3000)
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_E8(0xE8, 0x3, 0x0, 0x0)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C3605   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_1007 end

    def Function_10_12CE(): pass

    label("Function_10_12CE")

    Call(0, 11)
    Call(0, 12)
    Return()

    # Function_10_12CE end

    def Function_11_12D7(): pass

    label("Function_11_12D7")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12EE")
    Call(0, 13)
    Call(0, 14)

    label("loc_12EE")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_130F"),
        (5, "loc_1326"),
        (4, "loc_133D"),
        (6, "loc_1354"),
        (7, "loc_136B"),
        (8, "loc_1382"),
        (SWITCH_DEFAULT, "loc_1399"),
    )


    label("loc_130F")

    OP_D2(0x701D0, 0x701DC, 0xF)
    OP_D2(0x701D1, 0x701DD, 0x10)
    Jump("loc_1399")

    label("loc_1326")

    OP_D2(0x70218, 0x70224, 0xF)
    OP_D2(0x70219, 0x70225, 0x10)
    Jump("loc_1399")

    label("loc_133D")

    OP_D2(0x70200, 0x7020C, 0xF)
    OP_D2(0x70201, 0x7020D, 0x10)
    Jump("loc_1399")

    label("loc_1354")

    OP_D2(0x70230, 0x7023C, 0xF)
    OP_D2(0x70231, 0x7023D, 0x10)
    Jump("loc_1399")

    label("loc_136B")

    OP_D2(0x70248, 0x70254, 0xF)
    OP_D2(0x70249, 0x70255, 0x10)
    Jump("loc_1399")

    label("loc_1382")

    OP_D2(0x270176, 0x270183, 0xF)
    OP_D2(0x270177, 0x270184, 0x10)
    Jump("loc_1399")

    label("loc_1399")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_13BA"),
        (5, "loc_13D1"),
        (4, "loc_13E8"),
        (6, "loc_13FF"),
        (7, "loc_1416"),
        (8, "loc_142D"),
        (SWITCH_DEFAULT, "loc_1444"),
    )


    label("loc_13BA")

    OP_D2(0x701D0, 0x701DC, 0x11)
    OP_D2(0x701D1, 0x701DD, 0x12)
    Jump("loc_1444")

    label("loc_13D1")

    OP_D2(0x70218, 0x70224, 0x11)
    OP_D2(0x70219, 0x70225, 0x12)
    Jump("loc_1444")

    label("loc_13E8")

    OP_D2(0x70200, 0x7020C, 0x11)
    OP_D2(0x70201, 0x7020D, 0x12)
    Jump("loc_1444")

    label("loc_13FF")

    OP_D2(0x70230, 0x7023C, 0x11)
    OP_D2(0x70231, 0x7023D, 0x12)
    Jump("loc_1444")

    label("loc_1416")

    OP_D2(0x70248, 0x70254, 0x11)
    OP_D2(0x70249, 0x70255, 0x12)
    Jump("loc_1444")

    label("loc_142D")

    OP_D2(0x270176, 0x270183, 0x11)
    OP_D2(0x270177, 0x270184, 0x12)
    Jump("loc_1444")

    label("loc_1444")

    OP_D2(0x27026E, 0x270278, 0x13)
    OP_6D(720, 0, -6220, 0)
    OP_67(0, 9730, -10000, 0)
    OP_6B(1820, 0)
    OP_6C(45000, 0)
    OP_6E(500, 0)
    SetChrPos(0x8, 700, 950, 12150, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x101, -650, -1750, -7480, 0)
    SetChrPos(0x102, 740, -1750, -7480, 0)
    SetChrPos(0xF8, -750, -1750, -7480, 0)
    SetChrPos(0xF9, 820, -1750, -7480, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_71(0x5, 0x4)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_70(0x0, 0x8)
    OP_70(0x1, 0x8)
    OP_70(0x2, 0x8)
    OP_70(0x3, 0x8)
    OP_70(0x4, 0x8)
    LoadEffect(0x1, "map\\\\mp061_00.eff")
    PlayEffect(0x1, 0xFF, 0xFF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    FadeToBright(2000, 0)

    def lambda_159C():
        OP_6D(600, 0, -350, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_159C)
    ClearChrFlags(0x101, 0x80)

    def lambda_15B9():
        OP_8E(0xFE, 0xFFFFFEA2, 0x0, 0xFFFFF827, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15B9)
    Sleep(100)
    ClearChrFlags(0x102, 0x80)

    def lambda_15DE():
        OP_8E(0xFE, 0x3B6, 0x0, 0xFFFFF808, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15DE)
    Sleep(800)
    ClearChrFlags(0xF8, 0x80)

    def lambda_1603():
        OP_8E(0xFE, 0xFFFFFD12, 0x0, 0xFFFFF1FA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1603)
    Sleep(100)
    ClearChrFlags(0xF9, 0x80)

    def lambda_1628():
        OP_8E(0xFE, 0x334, 0x0, 0xFFFFF240, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1628)
    WaitChrThread(0xF9, 0x1)
    Sleep(500)

    ChrTalk(    #11
        0x101,
        "#1020F#5PIs this...the top of the tower?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16B3")

    ChrTalk(    #12
        0x109,
        "#1063F#2PI think so, but...look at it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1799")

    label("loc_16B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16ED")

    ChrTalk(    #13
        0x106,
        "#057F#2PThink so. The hell is this?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1799")

    label("loc_16ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1722")

    ChrTalk(    #14
        0x103,
        "#022F#2PIt must be. What on...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1799")

    label("loc_1722")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1762")

    ChrTalk(    #15
        0x108,
        "#072F#2PI believe so. Aidios preserve us.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1799")

    label("loc_1762")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1799")

    ChrTalk(    #16
        0x107,
        "#065F#2PI think so, but it's all...\x02",
    )

    CloseMessageWindow()

    label("loc_1799")


    ChrTalk(    #17
        0x102,
        (
            "#1043F#5PSo this is what they're hiding on the\x01",
            "roofs with these dark barriers.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #18
        0x8,
        "Man's Voice",
        "#4PHo ho. That was sprightly.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_187B")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_18B9")

    label("loc_187B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18A2")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_18B9")

    label("loc_18A2")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_18B9")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18E5")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1923")

    label("loc_18E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_190C")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1923")

    label("loc_190C")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1923")

    Sleep(1000)
    OP_1D(0x6F)
    Sleep(500)

    def lambda_1935():
        OP_6D(1800, 0, 8900, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1935)

    def lambda_194D():
        OP_67(0, 5400, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_194D)

    def lambda_1965():
        OP_6B(2520, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1965)
    Sleep(2500)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 3)

    def lambda_1984():
        OP_8E(0xFE, 0xFFFFFD44, 0x0, 0x122A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1984)
    Sleep(200)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 5)

    def lambda_19AE():
        OP_8E(0xFE, 0x2BC, 0x0, 0x11A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_19AE)
    Sleep(200)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF8, 15)

    def lambda_19D8():
        OP_8E(0xFE, 0xFFFFFCE0, 0x0, 0xB72, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_19D8)
    Sleep(200)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 17)

    def lambda_1A02():
        OP_8E(0xFE, 0x320, 0x0, 0xAF0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1A02)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #19
        0x101,
        "#1002F#2PSo you ARE here...you masked weirdo.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B72")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as cleared all of Bleublanc's Challenges\x01",            # 0
            "Set as clear one or more of Bleublanc's Challenges\x01",      # 1
            "Set as ignored Bleublanc's Challenges\x01",                   # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1B24"),
        (1, "loc_1B3B"),
        (2, "loc_1B52"),
        (SWITCH_DEFAULT, "loc_1B69"),
    )


    label("loc_1B24")

    OP_28(0x6C, 0x4, 0x10)
    OP_28(0x77, 0x4, 0x10)
    OP_28(0x78, 0x4, 0x10)
    OP_28(0xC4, 0x4, 0x10)
    Jump("loc_1B69")

    label("loc_1B3B")

    OP_28(0x6C, 0x4, 0x10)
    OP_28(0x77, 0x3, 0x10)
    OP_28(0x78, 0x3, 0x10)
    OP_28(0xC4, 0x3, 0x10)
    Jump("loc_1B69")

    label("loc_1B52")

    OP_28(0x6C, 0x3, 0x10)
    OP_28(0x77, 0x3, 0x10)
    OP_28(0x78, 0x3, 0x10)
    OP_28(0xC4, 0x3, 0x10)
    Jump("loc_1B69")

    label("loc_1B69")

    FadeToBright(300, 0)

    label("loc_1B72")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1B86")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1B86")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1B9A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1B9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1BAE")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1BAE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1BC2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1BC2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CC1")

    ChrTalk(    #20
        0x8,
        (
            "#232FHmmm. Must we trade insults?\x02\x03",

            "I would expect better from the ones who\x01",
            "managed to best every one of my challenges.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#1019F#2PThose 'challenges' are half the reason\x01",
            "I don't want to even bother talking to\x01",
            "you anymore, you know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E81")

    label("loc_1CC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DC9")

    ChrTalk(    #22
        0x8,
        (
            "#230FCome now, such shameful,\x01",
            "childish insults.\x02\x03",

            "We have traded wits in the past.\x01",
            "Can we not show one another\x01",
            "a little respect?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#1019F#2PForgive the hell out of me for\x01",
            "not showing respect to a weirdo\x01",
            "with an opera fetish, then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E81")

    label("loc_1DC9")


    ChrTalk(    #24
        0x8,
        (
            "#231FHow completely shameful your speech is.\x02\x03",

            "It is to be expected of those without\x01",
            "the courage to accept my challenges,\x01",
            "I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        "#1019F#2PMore like common friggin' SENSE!\x02",
    )

    CloseMessageWindow()

    label("loc_1E81")


    ChrTalk(    #26
        0x8,
        (
            "#230FPutting that aside...this is something\x01",
            "of an event, is it not?\x02\x03",

            "#231FIt has been an age since we last\x01",
            "met, after all...Joshua Astray,\x01",
            "Black Fang of Ouroboros.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        (
            "#1035F#2P...It has, hasn't it?\x02\x03",

            "#1042FI'll admit. I was surprised YOU would\x01",
            "support Weissmann's plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "#230FHah. Well. Putting anyone else aside,\x01",
            "I am here out of...curiosity.\x02\x03",

            "#233FThis land of Liberl possesses a mysterious\x01",
            "sort of dignity, wouldn't you agree?\x02\x03",

            "In the people, the land, even the air.\x02\x03",

            "#231FI simply wished to discern\x01",
            "if this dignity is real.\x02\x03",

            "For, when faced with disaster, it\x01",
            "should shine forth all the greater.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x102,
        (
            "#1042F#2PI...see.\x02\x03",

            "#1035FIn some ways, you're more like\x01",
            "Weissmann than I thought, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "#231FHahah! What I seek is beauty, in\x01",
            "all its forms. The good professor's\x01",
            "goals are...somewhat different.\x02\x03",

            "I should think that you, above all\x01",
            "others, would understand that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        "#1042F#2P...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27BE")

    ChrTalk(    #32
        0x8,
        (
            "#230FAh, and my darling princess\x01",
            "has come as well.\x02\x03",

            "May I assume that means you\x01",
            "shall accept my adoration?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x105,
        (
            "#047F#2PUnfortunately... I fear I cannot\x01",
            "live up to your expectations.\x02\x03",

            "#043FIf I were truly noble,\x01",
            "I would not...hesitate so.\x02\x03",

            "I shall have to give an answer\x01",
            "when I return the Arseille.\x02\x03",

            "#049FI... I dread that moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#1026F#5PKloe...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x102,
        "#1043F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "#231FHA-HA! Ahhhh! Yes! That fear!\x01",
            "O shining proof of nobility!\x02\x03",

            "O radiant wings which will not\x01",
            "deign to touch the disgusting\x01",
            "insects crawling in the mud!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 2)
    OP_0D()
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 19)
    OP_99(0x8, 0x0, 0xE, 0x7D0)

    def lambda_245F():
        OP_6D(1280, 0, 7850, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_245F)

    def lambda_2477():
        OP_67(0, 5250, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2477)

    def lambda_248F():
        OP_6B(2520, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_248F)
    SetChrPos(0x9, 6410, 8800, 5150, 270)
    SetChrPos(0xA, -6950, 8800, 3250, 90)
    OP_9F(0x9, 0xFF, 0x0, 0x0, 0x0, 0x0)
    OP_9F(0xA, 0xFF, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x4)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    def lambda_24EB():
        OP_96(0xFE, 0x190A, 0x320, 0x141E, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_24EB)
    OP_9F(0x9, 0x64, 0x64, 0xFF, 0xFF, 0x64)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
    WaitChrThread(0x9, 0x1)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_43(0x9, 0x3, 0x0, 0x2)

    def lambda_2541():
        OP_96(0xFE, 0xFFFFE4DA, 0x320, 0xCB2, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2541)
    OP_9F(0xA, 0x64, 0x64, 0xFF, 0xFF, 0x64)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
    WaitChrThread(0xA, 0x1)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_43(0xA, 0x3, 0x0, 0x2)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25F0")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_262E")

    label("loc_25F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2617")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_262E")

    label("loc_2617")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_262E")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_265A")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2698")

    label("loc_265A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2681")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2698")

    label("loc_2681")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2698")

    Sleep(1000)

    def lambda_26A3():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_26A3)
    Sleep(50)

    def lambda_26B6():
        OP_8C(0xFE, 90, 600)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_26B6)
    Sleep(50)

    def lambda_26C9():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_26C9)
    Sleep(50)

    def lambda_26DC():
        OP_8C(0xFE, 90, 600)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_26DC)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #37
        0x105,
        "#042F#5PAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#1020F#5PWaaaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x102,
        "#1046F#2PBalancing Clowns--assault archaisms!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 2)
    OP_0D()
    Sleep(500)

    ChrTalk(    #40
        0x8,
        (
            "#231FNow! Show me!\x02\x03",

            "Show me that radiance as it brings\x01",
            "light to this shadowed land!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F06")

    label("loc_27BE")


    ChrTalk(    #41
        0x8,
        (
            "#232FAnd you break my heart, as well!\x02\x03",

            "You must have known it was I who\x01",
            "was here.\x02\x03",

            "To know that and not bring\x01",
            "Her Highness, Princess Klaudia!\x01",
            "How rude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#1019F#2POh, you have GOT to be kidding.\x02\x03",

            "Who the heck would actually bring you Kloe,\x01",
            "you walking monument to perverse...itude!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_291A")

    ChrTalk(    #43
        0x107,
        "#065F#2PUmmm... (Wow,  he kinda is...)\x02",
    )

    CloseMessageWindow()

    label("loc_291A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_296A")

    ChrTalk(    #44
        0x108,
        (
            "#075F#2PThat is...shameless, to\x01",
            "say the least, Bleublanc.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A85")

    label("loc_296A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29C7")

    ChrTalk(    #45
        0x103,
        (
            "#025F#2P 'Perversitude'...is about the shape\x01",
            "of it. Have you NO shame?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A85")

    label("loc_29C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A1C")

    ChrTalk(    #46
        0x106,
        (
            "#551F#2PAin't there limits to how\x01",
            "shameless you can be, clown?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A85")

    label("loc_2A1C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A85")

    ChrTalk(    #47
        0x109,
        (
            "#1068F#2P'Perversitude.' Yeah, that...about sums\x01",
            "it up. He really is kinda shameless.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A85")


    ChrTalk(    #48
        0x102,
        (
            "#1035F#2PBleublanc...enough verbal fencing.\x02\x03",

            "#1042FWe are here to stop the society's plans.\x02\x03",

            "There's only one way we can settle this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        "#231FHeh heh. So there is.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 2)
    OP_0D()
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 19)
    OP_99(0x8, 0x0, 0xE, 0x7D0)

    def lambda_2B63():
        OP_6D(1280, 0, 7850, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2B63)

    def lambda_2B7B():
        OP_67(0, 5250, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B7B)

    def lambda_2B93():
        OP_6B(2520, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2B93)
    SetChrPos(0x9, 6410, 8800, 5150, 270)
    SetChrPos(0xA, -6950, 8800, 3250, 90)
    OP_9F(0x9, 0xFF, 0x0, 0x0, 0x0, 0x0)
    OP_9F(0xA, 0xFF, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x4)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    def lambda_2BEF():
        OP_96(0xFE, 0x190A, 0x320, 0x141E, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2BEF)
    OP_9F(0x9, 0x64, 0x64, 0xFF, 0xFF, 0x64)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
    WaitChrThread(0x9, 0x1)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_43(0x9, 0x3, 0x0, 0x2)

    def lambda_2C45():
        OP_96(0xFE, 0xFFFFE4DA, 0x320, 0xCB2, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2C45)
    OP_9F(0xA, 0x64, 0x64, 0xFF, 0xFF, 0x64)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
    WaitChrThread(0xA, 0x1)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_43(0xA, 0x3, 0x0, 0x2)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CF4")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2D32")

    label("loc_2CF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D1B")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2D32")

    label("loc_2D1B")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2D32")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D5E")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2D9C")

    label("loc_2D5E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D85")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2D9C")

    label("loc_2D85")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2D9C")

    Sleep(1000)

    def lambda_2DA7():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2DA7)
    Sleep(50)

    def lambda_2DBA():
        OP_8C(0xFE, 90, 600)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2DBA)
    Sleep(50)

    def lambda_2DCD():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_2DCD)
    Sleep(50)

    def lambda_2DE0():
        OP_8C(0xFE, 90, 600)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2DE0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #50
        0x101,
        "#1020F#5PWaaaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x102,
        "#1046F#2PBalancing Clowns--assault archaisms!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 2)
    OP_0D()
    Sleep(500)

    ChrTalk(    #52
        0x8,
        (
            "#231FO Black Fang...this is the first\x01",
            "time we have crossed sabers.\x02\x03",

            "I beseech you! Combine your might\x01",
            "with the Divine Blade's daughter,\x01",
            "and show me what nobility you have!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F06")


    def lambda_2F0C():
        OP_6D(440, 0, 5440, 300)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2F0C)

    def lambda_2F24():
        OP_6B(2000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F24)
    OP_22(0x23B, 0x0, 0x64)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 9)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)

    def lambda_2F4B():
        OP_96(0xFE, 0x1E, 0x0, 0x18CE, 0x5DC, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2F4B)
    Sleep(100)
    OP_44(0x9, 0x3)
    SetChrFlags(0x9, 0x1000)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 8)

    def lambda_2F81():
        OP_8E(0xFE, 0x5FA, 0x320, 0x1144, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2F81)
    OP_44(0xA, 0x3)
    SetChrFlags(0xA, 0x1000)
    SetChrSubChip(0xA, 0)
    SetChrChipByIndex(0xA, 8)

    def lambda_2FAF():
        OP_8E(0xFE, 0xFFFFF5B0, 0x320, 0xE10, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2FAF)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0x8, 0x1)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    Battle(0x454, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_2FFB"),
        (SWITCH_DEFAULT, "loc_3000"),
    )


    label("loc_2FFB")

    OP_B4(0x0)
    Jump("loc_3000")

    label("loc_3000")

    Return()

    # Function_11_12D7 end

    def Function_12_3001(): pass

    label("Function_12_3001")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(330, 200, 12720, 0)
    OP_67(0, 3720, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(0, 0)
    OP_6E(501, 0)
    OP_44(0x8, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0x1)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    OP_71(0x5, 0x4)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_70(0x0, 0x8)
    OP_70(0x1, 0x8)
    OP_70(0x2, 0x8)
    OP_70(0x3, 0x8)
    OP_70(0x4, 0x8)
    OP_7B()
    LoadEffect(0x1, "map\\\\mp061_00.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x8, 700, 950, 12150, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x101, -530, 0, 5830, 0)
    SetChrPos(0x102, 660, 0, 5640, 0)
    SetChrPos(0xF8, -790, 0, 3690, 0)
    SetChrPos(0xF9, 920, 0, 3630, 0)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_3170"),
        (5, "loc_317D"),
        (4, "loc_318A"),
        (6, "loc_3197"),
        (7, "loc_31A4"),
        (8, "loc_31B1"),
        (SWITCH_DEFAULT, "loc_31BE"),
    )


    label("loc_3170")

    OP_D2(0x701D0, 0x701DC, 0xF)
    Jump("loc_31BE")

    label("loc_317D")

    OP_D2(0x70218, 0x70224, 0xF)
    Jump("loc_31BE")

    label("loc_318A")

    OP_D2(0x70200, 0x7020C, 0xF)
    Jump("loc_31BE")

    label("loc_3197")

    OP_D2(0x70230, 0x7023C, 0xF)
    Jump("loc_31BE")

    label("loc_31A4")

    OP_D2(0x70248, 0x70254, 0xF)
    Jump("loc_31BE")

    label("loc_31B1")

    OP_D2(0x270176, 0x270183, 0xF)
    Jump("loc_31BE")

    label("loc_31BE")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_31DF"),
        (5, "loc_31EC"),
        (4, "loc_31F9"),
        (6, "loc_3206"),
        (7, "loc_3213"),
        (8, "loc_3220"),
        (SWITCH_DEFAULT, "loc_322D"),
    )


    label("loc_31DF")

    OP_D2(0x701D0, 0x701DC, 0x11)
    Jump("loc_322D")

    label("loc_31EC")

    OP_D2(0x70218, 0x70224, 0x11)
    Jump("loc_322D")

    label("loc_31F9")

    OP_D2(0x70200, 0x7020C, 0x11)
    Jump("loc_322D")

    label("loc_3206")

    OP_D2(0x70230, 0x7023C, 0x11)
    Jump("loc_322D")

    label("loc_3213")

    OP_D2(0x70248, 0x70254, 0x11)
    Jump("loc_322D")

    label("loc_3220")

    OP_D2(0x270176, 0x270183, 0x11)
    Jump("loc_322D")

    label("loc_322D")

    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 2)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 3)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 5)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF8, 15)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 17)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #53
        0x8,
        (
            "#230F#6POooh. More capable than I'd hoped for.\x02\x03",

            "#231FPerhaps it is time we get\x01",
            "properly serious, th--\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x99, 0x0, 0x64)
    OP_23(0xEB)
    OP_20(0x7D0)
    Fade(500)
    OP_6B(2500, 0)
    OP_82(0x1, 0x2)
    OP_82(0x81, 0x2)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x83, 0x2)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0x4, 0x2)
    OP_7B()
    Sleep(500)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3C)
    Sleep(500)
    OP_72(0x1, 0x20)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3C)
    Sleep(100)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x3C)
    Sleep(100)
    OP_72(0x3, 0x20)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x3C)
    Sleep(100)
    OP_72(0x4, 0x20)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x3C)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x8, 0, 600)
    Sleep(400)

    ChrTalk(    #54
        0x8,
        "#233F#6PHm?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x102,
        "#1042F#5P...!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(5030, 3860, 11650, 0)
    OP_67(0, 1590, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(43000, 0)
    OP_6E(363, 0)
    OP_0D()

    def lambda_348F():
        OP_6B(5500, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_348F)
    Sleep(500)
    OP_22(0x139, 0x0, 0x64)
    LoadEffect(0x2, "map\\mp049_02.eff")
    PlayEffect(0x2, 0x2, 0xFF, 0, 0, 6720, 0, 0, 0, 550, 550, 550, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    OP_82(0x80, 0x0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C0707   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_3001 end

    def Function_13_3510(): pass

    label("Function_13_3510")

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
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3589"),
        (1, "loc_358F"),
        (SWITCH_DEFAULT, "loc_3595"),
    )


    label("loc_3589")

    OP_A2(0x1200)
    Jump("loc_3595")

    label("loc_358F")

    OP_A2(0x1201)
    Jump("loc_3595")

    label("loc_3595")

    Return()

    # Function_13_3510 end

    def Function_14_3596(): pass

    label("Function_14_3596")

    FadeToDark(0, 0, -1)
    OP_6D(-66940, 250, 36210, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_14_3596 end

    SaveToFile()

Try(main)
