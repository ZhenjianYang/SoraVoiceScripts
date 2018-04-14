from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '幻惑之铃露茜奥拉',                     # 9
        '无形迷雾',                             # 10
        '气雾兽',                               # 11
        '福音',                                 # 12
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
        "Function_4_570",          # 04, 4
        "Function_5_81C",          # 05, 5
        "Function_6_825",          # 06, 6
        "Function_7_1561",         # 07, 7
        "Function_8_2156",         # 08, 8
        "Function_9_21DD",         # 09, 9
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
            "#240F#5P这里是『幻惑之铃』。\x02\x03",

            "『β』的设置完成了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C1705   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_3E6 end

    def Function_4_570(): pass

    label("Function_4_570")

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
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C1705   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_570 end

    def Function_5_81C(): pass

    label("Function_5_81C")

    Call(0, 6)
    Call(0, 7)
    Return()

    # Function_5_81C end

    def Function_6_825(): pass

    label("Function_6_825")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_83C")
    Call(0, 8)
    Call(0, 9)

    label("loc_83C")

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

    def lambda_981():
        OP_6D(430, 0, -2500, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_981)

    def lambda_999():
        OP_67(0, 8960, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_999)

    def lambda_9B1():
        OP_6B(2300, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9B1)

    def lambda_9C1():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9C1)

    def lambda_9D1():
        OP_6E(307, 5000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9D1)
    FadeToBright(1000, 0)
    Sleep(4000)
    ClearChrFlags(0x101, 0x80)

    def lambda_9F4():
        OP_8E(0xFE, 0x384, 0x0, 0xFFFFF808, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9F4)
    Sleep(100)
    ClearChrFlags(0x102, 0x80)

    def lambda_A19():
        OP_8E(0xFE, 0xFFFFFE3E, 0x0, 0xFFFFF827, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A19)
    Sleep(600)
    ClearChrFlags(0x103, 0x80)

    def lambda_A3E():
        OP_8E(0xFE, 0x352, 0x0, 0xFFFFF240, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A3E)
    Sleep(100)
    ClearChrFlags(0xF9, 0x80)

    def lambda_A63():
        OP_8E(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFF1FA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_A63)
    WaitChrThread(0xF9, 0x1)

    NpcTalk(    #1
        0x8,
        "女性的声音",
        (
            "呵呵……\x01",
            "好像稍微有些迟到了呢。\x02",
        )
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B28")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B66")

    label("loc_B28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4F")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B66")

    label("loc_B4F")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_B66")

    Sleep(1000)

    ChrTalk(    #2
        0x103,
        "#022F姐姐……！\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_1D(0x6F)
    Sleep(500)

    def lambda_B92():
        OP_6D(1160, 950, 13010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B92)

    def lambda_BAA():
        OP_67(0, 5350, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BAA)

    def lambda_BC2():
        OP_6E(337, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_BC2)
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
        (5, "loc_C50"),
        (4, "loc_C5D"),
        (6, "loc_C6A"),
        (7, "loc_C77"),
        (8, "loc_C84"),
        (SWITCH_DEFAULT, "loc_C91"),
    )


    label("loc_C50")

    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 14)
    Jump("loc_C91")

    label("loc_C5D")

    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x105, 16)
    Jump("loc_C91")

    label("loc_C6A")

    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 18)
    Jump("loc_C91")

    label("loc_C77")

    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 20)
    Jump("loc_C91")

    label("loc_C84")

    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x109, 22)
    Jump("loc_C91")

    label("loc_C91")


    def lambda_C97():
        OP_8E(0xFE, 0xFFFFFFB0, 0x0, 0xFA0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C97)
    Sleep(300)

    def lambda_CB7():
        OP_8E(0xFE, 0x3F2, 0x0, 0xD0C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CB7)
    Sleep(100)

    def lambda_CD7():
        OP_8E(0xFE, 0xFFFFFA88, 0x0, 0xAE6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CD7)
    Sleep(200)

    def lambda_CF7():
        OP_8E(0xFE, 0xFFFFFE98, 0x0, 0x88E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_CF7)
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
            "#240F欢迎，雪拉扎德。\x02\x03",

            "还有约修亚……\x01",
            "好久不见，真令人高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x102,
        (
            "#1042F#6P露茜奥拉……\x02\x03",

            "为什么你会\x01",
            "协助教授？\x02\x03",

            "我还以为你和教授的关系\x01",
            "没那么好呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#244F因为这里是我\x01",
            "巡回修业时曾经造访过的留恋之地……\x02\x03",

            "#241F所以忍不住来了兴致，\x01",
            "也就是这样的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#1005F#4P既、既然是留恋之地，\x01",
            "为什么还要帮教授做这种事！？\x02\x03",

            "也不顾忌一下雪拉姐的心情……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x103,
        (
            "#522F#6P艾丝蒂尔……算了。\x02\x03",

            "#022F光是动嘴，\x01",
            "姐姐是不会回答你任何问题的。\x02\x03",

            "除非我证明给她看\x01",
            "我的实力值得她回答。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#241F哎呀……呵呵呵。\x02\x03",

            "不愧是雪拉，\x01",
            "果然很了解我嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x103,
        (
            "#524F#6P以前姐姐教我技艺的时候\x01",
            "也总是这个样子的……\x02\x03",

            "#026F所以姐姐……答应我。\x02\x03",

            "#024F如果我能够证明自己实力的话，\x01",
            "那你就告诉我\x01",
            "为什么要帮助『结社』……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        "#244F呵呵……好啊。\x02",
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

    def lambda_11F2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_11F2)

    def lambda_1204():
        OP_8F(0xFE, 0xAF0, 0x5DC, 0x25B2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1204)
    Sleep(800)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_122E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_122E)

    def lambda_1240():
        OP_8F(0xFE, 0xFFFFFB50, 0x5DC, 0x2904, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1240)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12DA")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1318")

    label("loc_12DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1301")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1318")

    label("loc_1301")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1318")

    Sleep(1000)

    ChrTalk(    #11
        0x101,
        "#1020F#6P出，出现了……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        (
            "#1042F#6P善鬼与护鬼──\x01",
            "掌管阴阳的式神们！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "#244F这是将东方的符术\x01",
            "整理以后自成一派的东西哦。\x02\x03",

            "#240F雪拉扎德。\x01",
            "请让我看看。\x02\x03",

            "你离开我身边之后，\x01",
            "在这里到底获得了多少的能力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x103,
        (
            "#026F#6P……明白。\x02\x03",

            "#024F那我就献丑了，\x01",
            "看看我这『银闪』的实力吧！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_143F():
        OP_6D(950, 250, 11010, 300)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_143F)

    def lambda_1457():
        OP_67(0, 3510, -10000, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1457)

    def lambda_146F():
        OP_6B(2780, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_146F)

    def lambda_147F():
        OP_8F(0xFE, 0x2C6, 0x0, 0x1AB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_147F)
    Sleep(50)

    def lambda_149F():
        OP_8F(0xFE, 0x668, 0x0, 0x16B2, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_149F)

    def lambda_14BA():
        OP_8F(0xFE, 0xFFFFFE48, 0x0, 0x175C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14BA)

    def lambda_14D5():
        OP_8F(0xFE, 0xFFFFFF06, 0x64, 0x1F40, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_14D5)
    Sleep(50)

    def lambda_14F5():
        OP_8F(0xFE, 0x79E, 0x64, 0x2080, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_14F5)

    def lambda_1510():
        OP_8F(0xFE, 0x172, 0x0, 0x10D6, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1510)
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
        (1, "loc_155B"),
        (SWITCH_DEFAULT, "loc_1560"),
    )


    label("loc_155B")

    OP_B4(0x0)
    Jump("loc_1560")

    label("loc_1560")

    Return()

    # Function_6_825 end

    def Function_7_1561(): pass

    label("Function_7_1561")

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
        (5, "loc_15D4"),
        (4, "loc_15E1"),
        (6, "loc_15EE"),
        (7, "loc_15FB"),
        (8, "loc_1608"),
        (SWITCH_DEFAULT, "loc_1615"),
    )


    label("loc_15D4")

    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 14)
    Jump("loc_1615")

    label("loc_15E1")

    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x105, 16)
    Jump("loc_1615")

    label("loc_15EE")

    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 18)
    Jump("loc_1615")

    label("loc_15FB")

    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 20)
    Jump("loc_1615")

    label("loc_1608")

    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x109, 22)
    Jump("loc_1615")

    label("loc_1615")

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
            "#243F哎呀……\x01",
            "我的式神竟然被打倒了。\x02\x03",

            "#240F是拜『剑圣』的指导所赐吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        "#1022F#4P呼呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x103,
        "#024F#6P姐姐……如何！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#240F呵呵……\x01",
            "作为你努力的褒奖，我就告诉你吧。\x02\x03",

            "#244F我加入『结社』……\x01",
            "是想看清自己的黑暗面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x103,
        "#023F#6P咦……\x02",
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
        (5, "loc_189B"),
        (4, "loc_18A8"),
        (6, "loc_18B5"),
        (7, "loc_18C2"),
        (8, "loc_18CF"),
        (SWITCH_DEFAULT, "loc_18DC"),
    )


    label("loc_189B")

    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 14)
    Jump("loc_18DC")

    label("loc_18A8")

    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x105, 16)
    Jump("loc_18DC")

    label("loc_18B5")

    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 18)
    Jump("loc_18DC")

    label("loc_18C2")

    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 20)
    Jump("loc_18DC")

    label("loc_18CF")

    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x109, 22)
    Jump("loc_18DC")

    label("loc_18DC")

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
            "#242F#5P８年前……\x02\x03",

            "团长从悬崖摔落\x01",
            "而亡的事你还记得吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x103,
        (
            "#024F当、当然记得。\x02\x03",

            "由于那个事故，\x01",
            "我们哈维剧团的全体团员都……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "#244F#5P对……剧团解散，\x01",
            "大家都各奔东西了。\x02\x03",

            "但是，为何团长会独自一人\x01",
            "去那种渺无人烟的地方，\x01",
            "到最后谁也不明白……\x02\x03",

            "#240F你觉得这到底是怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x103,
        "#023F怎、怎么回事……\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_21()

    ChrTalk(    #24
        0x8,
        (
            "#244F#5P答案很简单……\x02\x03",

            "#241F那时，团长并不是\x01",
            "独自一人呆在悬崖附近。\x02\x03",

            "我就在他旁边……\x01",
            "并且把他推了下去。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1ACE():
        OP_6B(3200, 20000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1ACE)
    Sleep(200)
    OP_1D(0x53)
    Sleep(1000)

    ChrTalk(    #25
        0x103,
        (
            "#023F#6P……………………………\x02\x03",

            "……什么……\x01",
            "你在说什么呢，姐姐？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "#241F#5P呵呵，我不是说了吗。\x02\x03",

            "哈维团长\x01",
            "是我亲手杀死的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x103,
        (
            "#524F#6P啊哈哈……玩笑开过火了吧。\x02\x03",

            "因为那个时候，姐姐你……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "#244F#5P亲手杀害团长后，\x01",
            "我一脸平静地回到大家身边。\x02\x03",

            "然后就鸣响了铃铛，\x01",
            "让大家听到团长在喊叫的幻音。\x02\x03",

            "#241F──利用我的幻术，\x01",
            "要制造这点小把戏简直是轻而易举的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x103,
        (
            "#527F#6P住口……别再说了啊！\x02\x03",

            "姐姐竟然杀了团长……\x01",
            "怎么可能有这种事！\x02\x03",

            "#024F你们就像真正的父女一样……\x01",
            "甚至比真正的父女还要亲密！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "#242F#5P正因为如此，我才不能饶恕他。\x02\x03",

            "他竟然打算\x01",
            "离开我们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x103,
        "#023F#6P咦……\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E7B")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1EB9")

    label("loc_1E7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EA2")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1EB9")

    label("loc_1EA2")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1EB9")

    Sleep(1000)

    def lambda_1EC4():
        OP_6D(-250, 200, 17430, 2500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1EC4)

    def lambda_1EDC():
        OP_67(0, 3660, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1EDC)

    def lambda_1EF4():
        OP_6B(3460, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1EF4)
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
        "#1020F#5P又……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FC8")

    ChrTalk(    #33
        0x106,
        "#054F#5P恢复了吗……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_207C")

    label("loc_1FC8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FF5")

    ChrTalk(    #34
        0x107,
        "#065F#5P恢复了……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_207C")

    label("loc_1FF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2024")

    ChrTalk(    #35
        0x105,
        "#043F#5P恢复了吗……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_207C")

    label("loc_2024")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2051")

    ChrTalk(    #36
        0x108,
        "#072F#5P恢复了吗……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_207C")

    label("loc_2051")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_207C")

    ChrTalk(    #37
        0x109,
        "#1069F#5P恢复了吗……！\x02",
    )

    CloseMessageWindow()

    label("loc_207C")

    Sleep(300)
    OP_1F(0x64, 0x7D0)
    Fade(1000)
    OP_6D(5030, 3860, 11650, 0)
    OP_67(0, 1590, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(45000, 0)
    OP_6E(363, 0)
    OP_0D()

    def lambda_20D0():
        OP_6B(5500, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_20D0)
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

    # Function_7_1561 end

    def Function_8_2156(): pass

    label("Function_8_2156")

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
        (0, "loc_21D0"),
        (1, "loc_21D6"),
        (SWITCH_DEFAULT, "loc_21DC"),
    )


    label("loc_21D0")

    OP_A2(0x1200)
    Jump("loc_21DC")

    label("loc_21D6")

    OP_A2(0x1201)
    Jump("loc_21DC")

    label("loc_21DC")

    Return()

    # Function_8_2156 end

    def Function_9_21DD(): pass

    label("Function_9_21DD")

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

    # Function_9_21DD end

    SaveToFile()

Try(main)
