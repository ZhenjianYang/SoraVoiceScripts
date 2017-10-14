from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'C2305   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2305.x',
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
        'Luciola',                              # 9
        'Jubokko ',                             # 10
        'Zaqqum',                               # 11
        'Gospel',                               # 12
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
        'ED6_DT27/CH03520 ._CH',             # 00
        'ED6_DT29/CH12380 ._CH',             # 01
        'ED6_DT09/CH10910 ._CH',             # 02
        'ED6_DT06/CH20021 ._CH',             # 03
        'ED6_DT27/CH04520 ._CH',             # 04
        'ED6_DT27/CH04525 ._CH',             # 05
        'ED6_DT27/CH04526 ._CH',             # 06
        'ED6_DT27/CH04000 ._CH',             # 07
        'ED6_DT27/CH04001 ._CH',             # 08
        'ED6_DT27/CH04010 ._CH',             # 09
        'ED6_DT27/CH04011 ._CH',             # 0A
        'ED6_DT07/CH00120 ._CH',             # 0B
        'ED6_DT07/CH00121 ._CH',             # 0C
        'ED6_DT27/CH03523 ._CH',             # 0D
        'ED6_DT07/CH00150 ._CH',             # 0E
        'ED6_DT07/CH00151 ._CH',             # 0F
        'ED6_DT07/CH00140 ._CH',             # 10
        'ED6_DT07/CH00141 ._CH',             # 11
        'ED6_DT07/CH00160 ._CH',             # 12
        'ED6_DT07/CH00161 ._CH',             # 13
        'ED6_DT07/CH00170 ._CH',             # 14
        'ED6_DT07/CH00171 ._CH',             # 15
        'ED6_DT27/CH04080 ._CH',             # 16
        'ED6_DT27/CH04081 ._CH',             # 17
    )

    AddCharChipPat(
        'ED6_DT27/CH03520P._CP',             # 00
        'ED6_DT29/CH12380P._CP',             # 01
        'ED6_DT09/CH10910P._CP',             # 02
        'ED6_DT06/CH20021P._CP',             # 03
        'ED6_DT27/CH04520P._CP',             # 04
        'ED6_DT27/CH04525P._CP',             # 05
        'ED6_DT27/CH04526P._CP',             # 06
        'ED6_DT27/CH04000P._CP',             # 07
        'ED6_DT27/CH04001P._CP',             # 08
        'ED6_DT27/CH04010P._CP',             # 09
        'ED6_DT27/CH04011P._CP',             # 0A
        'ED6_DT07/CH00120P._CP',             # 0B
        'ED6_DT07/CH00121P._CP',             # 0C
        'ED6_DT27/CH03523P._CP',             # 0D
        'ED6_DT07/CH00150P._CP',             # 0E
        'ED6_DT07/CH00151P._CP',             # 0F
        'ED6_DT07/CH00140P._CP',             # 10
        'ED6_DT07/CH00141P._CP',             # 11
        'ED6_DT07/CH00160P._CP',             # 12
        'ED6_DT07/CH00161P._CP',             # 13
        'ED6_DT07/CH00170P._CP',             # 14
        'ED6_DT07/CH00171P._CP',             # 15
        'ED6_DT27/CH04080P._CP',             # 16
        'ED6_DT27/CH04081P._CP',             # 17
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
        Unknown3            = 458755,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1EA",          # 00, 0
        "Function_1_242",          # 01, 1
        "Function_2_269",          # 02, 2
        "Function_3_3E6",          # 03, 3
        "Function_4_575",          # 04, 4
        "Function_5_82F",          # 05, 5
        "Function_6_838",          # 06, 6
        "Function_7_16D4",         # 07, 7
        "Function_8_24FD",         # 08, 8
        "Function_9_2583",         # 09, 9
    )


    def Function_0_1EA(): pass

    label("Function_0_1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_209")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_241")

    label("loc_209")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_228")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 4)
    Jump("loc_241")

    label("loc_228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 3)), scpexpr(EXPR_END)), "loc_241")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 5)

    label("loc_241")

    Return()

    # Function_0_1EA end

    def Function_1_242(): pass

    label("Function_1_242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_253")
    OP_22(0xEB, 0x1, 0x50)

    label("loc_253")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x456), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_268")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_268")

    Return()

    # Function_1_242 end

    def Function_2_269(): pass

    label("Function_2_269")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28E")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_3D0")

    label("loc_28E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A7")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_3D0")

    label("loc_2A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C0")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_3D0")

    label("loc_2C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D9")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_3D0")

    label("loc_2D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F2")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_3D0")

    label("loc_2F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30B")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_3D0")

    label("loc_30B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_324")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_3D0")

    label("loc_324")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33D")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_3D0")

    label("loc_33D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_356")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_3D0")

    label("loc_356")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36F")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_3D0")

    label("loc_36F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_388")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_3D0")

    label("loc_388")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A1")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_3D0")

    label("loc_3A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BA")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_3D0")

    label("loc_3BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D0")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_3D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E5")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3D0")

    label("loc_3E5")

    Return()

    # Function_2_269 end

    def Function_3_3E6(): pass

    label("Function_3_3E6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(19060, 250, 11220, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4370, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_22(0x1C3, 0x0, 0x64)
    SetChrPos(0x8, -1120, 250, 10980, 180)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 13)
    SetChrSubChip(0x8, 1)
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

    def lambda_4A9():
        OP_6D(2600, 250, 13480, 4000)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_4A9)
    OP_C8(0x200, 0x46, "C_PLAC20._CH", 0x1, 0x3E8)
    FadeToBright(1000, 0)
    WaitChrThread(0xB, 0x0)
    Sleep(1000)
    Fade(1000)
    OP_6D(-1530, 0, 15630, 0)
    OP_67(0, 4400, -10000, 0)
    OP_6B(5730, 0)
    OP_6C(332000, 0)
    OP_6E(155, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x8,
        (
            "#240F#5PThis is Bewitching Bell.\x02\x03",

            "The beta is in place.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C1705   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_3E6 end

    def Function_4_575(): pass

    label("Function_4_575")

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
    SetChrPos(0x8, -1120, 250, 10980, 180)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 13)
    SetChrSubChip(0x8, 1)
    OP_E5(0x8, 0x0, 0x0)
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
    OP_E8(0xD0, 0x7, 0x0, 0x0)
    LoadEffect(0x1, "map\\\\mp061_00.eff")
    PlayEffect(0x1, 0xFF, 0xFF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
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
    NewScene("ED6_DT21/C1705   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_575 end

    def Function_5_82F(): pass

    label("Function_5_82F")

    Call(0, 6)
    Call(0, 7)
    Return()

    # Function_5_82F end

    def Function_6_838(): pass

    label("Function_6_838")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_84F")
    Call(0, 8)
    Call(0, 9)

    label("loc_84F")

    OP_6D(6870, 6810, 600, 0)
    OP_67(0, 4710, -10000, 0)
    OP_6B(2480, 0)
    OP_6C(56000, 0)
    OP_6E(386, 0)
    SetChrPos(0x8, 900, 950, 12280, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x101, 740, -1750, -7480, 0)
    SetChrPos(0x102, -650, -1750, -7480, 0)
    SetChrPos(0x103, 820, -1750, -7480, 0)
    SetChrPos(0xF9, -750, -1750, -7480, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xF9, 0x80)
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
    LoadEffect(0x0, "map\\\\mp061_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_71(0x5, 0x4)

    def lambda_994():
        OP_6D(430, 0, -2500, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_994)

    def lambda_9AC():
        OP_67(0, 8960, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9AC)

    def lambda_9C4():
        OP_6B(2300, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9C4)

    def lambda_9D4():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9D4)

    def lambda_9E4():
        OP_6E(307, 5000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9E4)
    FadeToBright(1000, 0)
    Sleep(4000)
    ClearChrFlags(0x101, 0x80)

    def lambda_A07():
        OP_8E(0xFE, 0x384, 0x0, 0xFFFFF808, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A07)
    Sleep(100)
    ClearChrFlags(0x102, 0x80)

    def lambda_A2C():
        OP_8E(0xFE, 0xFFFFFE3E, 0x0, 0xFFFFF827, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A2C)
    Sleep(600)
    ClearChrFlags(0x103, 0x80)

    def lambda_A51():
        OP_8E(0xFE, 0x352, 0x0, 0xFFFFF240, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A51)
    Sleep(100)
    ClearChrFlags(0xF9, 0x80)

    def lambda_A76():
        OP_8E(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFF1FA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_A76)
    WaitChrThread(0xF9, 0x1)

    NpcTalk(    #1
        0x8,
        "Woman's Voice",
        "You're a bit late, loves.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B38")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B76")

    label("loc_B38")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B5F")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B76")

    label("loc_B5F")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_B76")

    Sleep(1000)

    ChrTalk(    #2
        0x103,
        "#022FLuci...\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_1D(0x6F)
    Sleep(500)

    def lambda_B9F():
        OP_6D(1160, 950, 13010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B9F)

    def lambda_BB7():
        OP_67(0, 5350, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BB7)

    def lambda_BCF():
        OP_6E(337, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_BCF)
    WaitChrThread(0x101, 0x3)
    SetChrPos(0x103, 740, -1750, -7480, 0)
    SetChrPos(0x102, -650, -1750, -7480, 0)
    SetChrPos(0x101, 820, -1750, -7480, 0)
    SetChrPos(0xF9, -750, -1750, -7480, 0)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 7)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 9)
    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x103, 11)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (5, "loc_C5D"),
        (4, "loc_C6A"),
        (6, "loc_C77"),
        (7, "loc_C84"),
        (8, "loc_C91"),
        (SWITCH_DEFAULT, "loc_C9E"),
    )


    label("loc_C5D")

    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 14)
    Jump("loc_C9E")

    label("loc_C6A")

    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x105, 16)
    Jump("loc_C9E")

    label("loc_C77")

    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 18)
    Jump("loc_C9E")

    label("loc_C84")

    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 20)
    Jump("loc_C9E")

    label("loc_C91")

    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x109, 22)
    Jump("loc_C9E")

    label("loc_C9E")


    def lambda_CA4():
        OP_8E(0xFE, 0xFFFFFFB0, 0x0, 0xFA0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CA4)
    Sleep(300)

    def lambda_CC4():
        OP_8E(0xFE, 0x3F2, 0x0, 0xD0C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CC4)
    Sleep(100)

    def lambda_CE4():
        OP_8E(0xFE, 0xFFFFFA88, 0x0, 0xAE6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CE4)
    Sleep(200)

    def lambda_D04():
        OP_8E(0xFE, 0xFFFFFE98, 0x0, 0x88E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_D04)
    Fade(500)
    OP_6D(1610, 500, 9000, 0)
    OP_67(0, 2630, -10000, 0)
    OP_6B(2380, 0)
    OP_6C(29000, 0)
    OP_6E(452, 0)
    OP_0D()
    WaitChrThread(0xF9, 0x1)
    Sleep(500)

    ChrTalk(    #3
        0x8,
        (
            "#240FWelcome, Scherazard.\x02\x03",

            "And Joshua.\x01",
            "It IS good to see you again, and safe.\x01",
            "You were gone for far too long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x102,
        (
            "#1042F#2PLuciola...\x02\x03",

            "Why are you, of all people,\x01",
            "working with Weissmann?\x02\x03",

            "You and he never seemed\x01",
            "that close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#244FThis land is a nostalgic place for me,\x01",
            "I suppose. We came here so often in\x01",
            "our travels.\x02\x03",

            "#241FI suppose you could just\x01",
            "call it a whim of mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#1005F#2P'Nostalgic place,' my ass! Why are\x01",
            "you hurting it so much, then?!\x02\x03",

            "Are you even thinking about\x01",
            "how Schera feels abo--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x103,
        (
            "#522F#2PEstelle. Enough.\x02\x03",

            "#022FWords alone won't get any\x01",
            "answers from Luci.\x02\x03",

            "We have to prove we've enough\x01",
            "skill to be worthy of an answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#241FOh, my.\x02\x03",

            "You really haven't forgotten,\x01",
            "have you, Scherazard?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x103,
        (
            "#524F#2PJust like when you were teaching\x01",
            "me to perform, all those years ago...\x02\x03",

            "#026FSo, Luci...promise me.\x02\x03",

            "#024FIf I can prove my worth, tell me\x01",
            "why you're supporting the society!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        "#244FHmm hmm hmm... Very well.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(1000, 750, 11580, 0)
    OP_67(0, 2320, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(8000, 0)
    OP_6E(333, 0)
    OP_6D(1000, 750, 11580, 0)
    OP_67(0, 2280, -10000, 0)
    OP_6B(3380, 0)
    OP_6C(8000, 0)
    OP_6E(333, 0)
    SetChrPos(0x103, 100, 0, 3510, 0)
    SetChrPos(0x102, -1200, 0, 2900, 0)
    SetChrPos(0x101, 1000, 0, 2800, 0)
    SetChrPos(0xF9, -500, 0, 1500, 0)
    OP_0D()
    Sleep(200)
    Fade(250)
    SetChrSubChip(0x8, 3)
    SetChrChipByIndex(0x8, 5)
    OP_0D()
    LoadEffect(0x1, "scraft\\sc040_08.eff")
    PlayEffect(0x1, 0x0, 0xFF, -46660, 1000, 19260, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x265, 0x0, 0x64)
    Sleep(2000)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 6)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    Fade(500)
    OP_82(0x0, 0x2)
    OP_43(0x9, 0x3, 0x0, 0x2)
    SetChrPos(0x9, 2800, 2500, 9650, 180)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x9, 0x4)
    ClearChrFlags(0x9, 0x80)
    OP_43(0xA, 0x3, 0x0, 0x2)
    SetChrPos(0xA, -1200, 2500, 10500, 180)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xA, 0x4)
    ClearChrFlags(0xA, 0x80)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_12EF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_12EF)

    def lambda_1301():
        OP_8F(0xFE, 0xAF0, 0x5DC, 0x25B2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1301)
    Sleep(800)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_132B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_132B)

    def lambda_133D():
        OP_8F(0xFE, 0xFFFFFB50, 0x5DC, 0x2904, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_133D)
    Sleep(800)
    OP_22(0x21A, 0x0, 0x64)
    Sleep(800)
    OP_22(0x21A, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13D7")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1415")

    label("loc_13D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13FE")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1415")

    label("loc_13FE")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1415")

    Sleep(1000)

    ChrTalk(    #11
        0x101,
        "#1020F#2PWhat in the...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        (
            "#1042F#5PI recognize those. They're bound spirits,\x01",
            "in the forms of the guardians of light and\x01",
            "darkness from the Eastern lands!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "#244FYes, I added my own touch\x01",
            "to the charm arts of the East.\x02\x03",

            "#240FScherazard. Show me.\x02\x03",

            "Show me what you gained in\x01",
            "this land after you left me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x103,
        (
            "#026F#5P...All right.\x02\x03",

            "#024FDon't look away, then!\x01",
            "Or you'll miss the Silver Streak!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_15B2():
        OP_6D(950, 250, 11010, 300)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_15B2)

    def lambda_15CA():
        OP_67(0, 3510, -10000, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_15CA)

    def lambda_15E2():
        OP_6B(2780, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_15E2)

    def lambda_15F2():
        OP_8F(0xFE, 0x2C6, 0x0, 0x1AB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_15F2)
    Sleep(50)

    def lambda_1612():
        OP_8F(0xFE, 0x668, 0x0, 0x16B2, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1612)

    def lambda_162D():
        OP_8F(0xFE, 0xFFFFFE48, 0x0, 0x175C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_162D)

    def lambda_1648():
        OP_8F(0xFE, 0xFFFFFF06, 0x64, 0x1F40, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1648)
    Sleep(50)

    def lambda_1668():
        OP_8F(0xFE, 0x79E, 0x64, 0x2080, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1668)

    def lambda_1683():
        OP_8F(0xFE, 0x172, 0x0, 0x10D6, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1683)
    WaitChrThread(0x101, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0xF9, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x456, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_16CE"),
        (SWITCH_DEFAULT, "loc_16D3"),
    )


    label("loc_16CE")

    OP_B4(0x0)
    Jump("loc_16D3")

    label("loc_16D3")

    Return()

    # Function_6_838 end

    def Function_7_16D4(): pass

    label("Function_7_16D4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0x1)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    OP_44(0x103, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF9, 0x1)
    Sleep(500)
    Sleep(500)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 7)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 9)
    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x103, 11)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (5, "loc_1747"),
        (4, "loc_1754"),
        (6, "loc_1761"),
        (7, "loc_176E"),
        (8, "loc_177B"),
        (SWITCH_DEFAULT, "loc_1788"),
    )


    label("loc_1747")

    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 14)
    Jump("loc_1788")

    label("loc_1754")

    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x105, 16)
    Jump("loc_1788")

    label("loc_1761")

    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 18)
    Jump("loc_1788")

    label("loc_176E")

    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 20)
    Jump("loc_1788")

    label("loc_177B")

    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x109, 22)
    Jump("loc_1788")

    label("loc_1788")

    SetChrPos(0x103, -100, 0, 5100, 0)
    SetChrPos(0x101, 1200, 0, 4000, 0)
    SetChrPos(0x102, -1020, 0, 3400, 0)
    SetChrPos(0xF9, 200, 0, 2300, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 900, 950, 12280, 180)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 4)
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
    LoadEffect(0x0, "map\\\\mp061_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_6D(1280, 950, 9610, 0)
    OP_67(0, 4910, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(344, 0)
    OP_71(0x5, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #15
        0x8,
        (
            "#243FGoodness. You managed to\x01",
            "defeat my little spirits after all.\x02\x03",

            "#240FYou learned much from\x01",
            "the Divine Blade, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        "#1022F#2PHaah... Don't...doubt us! *pant*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x103,
        "#024F#2PWell, Luci? Is that enough for you?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#240FHmm... Yes, you have\x01",
            "earned your answer, I think.\x02\x03",

            "#244FI joined the society...to better\x01",
            "understand my own darkness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x103,
        "#023F#2PYour...what?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 7)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 9)
    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x103, 11)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (5, "loc_1A92"),
        (4, "loc_1A9F"),
        (6, "loc_1AAC"),
        (7, "loc_1AB9"),
        (8, "loc_1AC6"),
        (SWITCH_DEFAULT, "loc_1AD3"),
    )


    label("loc_1A92")

    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 14)
    Jump("loc_1AD3")

    label("loc_1A9F")

    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x105, 16)
    Jump("loc_1AD3")

    label("loc_1AAC")

    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 18)
    Jump("loc_1AD3")

    label("loc_1AB9")

    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 20)
    Jump("loc_1AD3")

    label("loc_1AC6")

    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x109, 22)
    Jump("loc_1AD3")

    label("loc_1AD3")

    OP_6D(110, 250, 12650, 0)
    OP_67(0, 3200, -10000, 0)
    OP_6B(3420, 0)
    OP_6C(0, 0)
    OP_6E(344, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #20
        0x8,
        (
            "#242F#6PYou remember eight years ago, of course.\x02\x03",

            "How the leader of our troupe\x01",
            "perished falling from a cliff?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x103,
        (
            "#024FOf course I do!\x01",
            "How could I forget?!\x02\x03",

            "That accident caused the Harvey Troupe to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "#244F#6PYes. It caused the troupe to disband\x01",
            "and go our separate ways.\x02\x03",

            "No one could ever figure out,\x01",
            "however, why he went to such\x01",
            "a lonely spot all on his own...\x02\x03",

            "#240FWhy do you think that was?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x103,
        "#023FI... I don't really...\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_21()

    ChrTalk(    #24
        0x8,
        (
            "#244F#6PYou can see the answer,\x01",
            "Schera. Acknowledge it.\x02\x03",

            "#241FThe troupe leader was not\x01",
            "alone on the cliff side.\x02\x03",

            "I was with him.\x01",
            "And I was the one who pushed him off.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1D89():
        OP_6B(3200, 20000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D89)
    Sleep(200)
    OP_1D(0x53)
    Sleep(1000)

    ChrTalk(    #25
        0x103,
        (
            "#023F#5P.    .    .\x02\x03",

            "What...are you...saying, Luci?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "#241F#6PTsk tsk. Were you not listening?\x02\x03",

            "I killed Harvey with my own hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x103,
        (
            "#524F#5PAh...ha ha ha...\x01",
            "Luci, come on. There's no need for\x01",
            "dark humor or trying to 'sound' evil.\x02\x03",

            "I mean, that's impossible, you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "#244F#6PAfter I pushed Harvey to his death,\x01",
            "I returned to camp, feeling almost nothing.\x01",
            "No one questioned my calm face.\x02\x03",

            "And then I used my bell to create an aural\x01",
            "illusion of his scream for all to hear.\x02\x03",

            "#241FReally almost trivial, with my skill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x103,
        (
            "#527F#5PStop... STOP!\x02\x03",

            "YOU killed Mr. Harvey? You?\x01",
            "No. No! Impossible! IDIOTIC!\x02\x03",

            "#024FYou were like parent and child...\x01",
            "no, even closer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "#242F#6PYes. So we were. And that is\x01",
            "why I couldn't forgive him.\x02\x03",

            "I couldn't forgive him for\x01",
            "planning to leave us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x103,
        "#023F#5PWhat...?\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0x2)
    Sleep(500)
    OP_22(0x99, 0x0, 0x64)
    OP_23(0xEB)
    OP_1F(0x5A, 0x7D0)
    Fade(500)
    OP_6B(3000, 0)
    OP_82(0x0, 0x2)
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
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2218")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2256")

    label("loc_2218")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_223F")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2256")

    label("loc_223F")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2256")

    Sleep(1000)

    def lambda_2261():
        OP_6D(-250, 200, 17430, 2500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2261)

    def lambda_2279():
        OP_67(0, 3660, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2279)

    def lambda_2291():
        OP_6B(3460, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2291)
    OP_8C(0x8, 270, 400)
    OP_8C(0x8, 0, 400)
    WaitChrThread(0x101, 0x0)
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

    ChrTalk(    #32
        0x101,
        "#1020F#5PAgain!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2363")

    ChrTalk(    #33
        0x106,
        "#054F#5PIt's shifting!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2423")

    label("loc_2363")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2390")

    ChrTalk(    #34
        0x107,
        "#065F#5PIt's shifting!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2423")

    label("loc_2390")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23C3")

    ChrTalk(    #35
        0x105,
        "#043F#5PIt must be shifting!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2423")

    label("loc_23C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23F2")

    ChrTalk(    #36
        0x108,
        "#072F#5PIt is reverting!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2423")

    label("loc_23F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2423")

    ChrTalk(    #37
        0x109,
        "#1069F#5PThink it's shifting!\x02",
    )

    CloseMessageWindow()

    label("loc_2423")

    Sleep(300)
    OP_1F(0x64, 0x7D0)
    Fade(1000)
    OP_6D(5030, 3860, 11650, 0)
    OP_67(0, 1590, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(45000, 0)
    OP_6E(363, 0)
    OP_0D()

    def lambda_2477():
        OP_6B(5500, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2477)
    Sleep(500)
    OP_22(0x139, 0x0, 0x64)
    LoadEffect(0x2, "map\\mp049_02.eff")
    PlayEffect(0x2, 0x2, 0xFF, 0, 0, 6720, 0, 0, 0, 550, 550, 550, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    OP_82(0x80, 0x0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C2307   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_16D4 end

    def Function_8_24FD(): pass

    label("Function_8_24FD")

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
        (0, "loc_2576"),
        (1, "loc_257C"),
        (SWITCH_DEFAULT, "loc_2582"),
    )


    label("loc_2576")

    OP_A2(0x1200)
    Jump("loc_2582")

    label("loc_257C")

    OP_A2(0x1201)
    Jump("loc_2582")

    label("loc_2582")

    Return()

    # Function_8_24FD end

    def Function_9_2583(): pass

    label("Function_9_2583")

    FadeToDark(0, 0, -1)
    OP_6D(-66940, 250, 36210, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0x2, 0xFF, 0x5, 0x6, 0x4, 0x8, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_9_2583 end

    SaveToFile()

Try(main)
