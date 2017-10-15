from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5409   ._SN',
        MapName             = 'Other',
        Location            = 'C5409.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60028",
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
        'Pale Apache',                          # 9
        'Pale Apache',                          # 10
        'Pale Apache',                          # 11
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
        'ED6_DT29/CH12390 ._CH',             # 00
        'ED6_DT29/CH12391 ._CH',             # 01
        'ED6_DT27/CH04000 ._CH',             # 02
        'ED6_DT27/CH04010 ._CH',             # 03
        'ED6_DT07/CH00310 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT29/CH12390P._CP',             # 00
        'ED6_DT29/CH12391P._CP',             # 01
        'ED6_DT27/CH04000P._CP',             # 02
        'ED6_DT27/CH04010P._CP',             # 03
        'ED6_DT07/CH00310P._CP',             # 04
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
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -8100,
        Y                   = 0,
        Z                   = -54880,
        Range               = 9750,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF3170,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )


    ScpFunction(
        "Function_0_152",          # 00, 0
        "Function_1_153",          # 01, 1
        "Function_2_1AF",          # 02, 2
        "Function_3_595",          # 03, 3
        "Function_4_5C5",          # 04, 4
        "Function_5_5F5",          # 05, 5
        "Function_6_625",          # 06, 6
        "Function_7_709",          # 07, 7
        "Function_8_7EA",          # 08, 8
        "Function_9_870",          # 09, 9
    )


    def Function_0_152(): pass

    label("Function_0_152")

    Return()

    # Function_0_152 end

    def Function_1_153(): pass

    label("Function_1_153")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_171")
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x10A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_171")

    OP_22(0x131, 0x1, 0x3C)
    OP_22(0x1C3, 0x1, 0x64)
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_153 end

    def Function_2_1AF(): pass

    label("Function_2_1AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BC")
    Return()

    label("loc_1BC")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E1")
    Call(0, 8)
    Call(0, 9)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_1E1")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_206"),
        (3, "loc_213"),
        (4, "loc_220"),
        (5, "loc_22D"),
        (6, "loc_23A"),
        (7, "loc_247"),
        (8, "loc_254"),
        (SWITCH_DEFAULT, "loc_261"),
    )


    label("loc_206")

    OP_D2(0x701D0, 0x701DC, 0x5)
    Jump("loc_261")

    label("loc_213")

    OP_D2(0x701E8, 0x701F4, 0x5)
    Jump("loc_261")

    label("loc_220")

    OP_D2(0x27036E, 0x27037B, 0x5)
    Jump("loc_261")

    label("loc_22D")

    OP_D2(0x70218, 0x70224, 0x5)
    Jump("loc_261")

    label("loc_23A")

    OP_D2(0x70230, 0x7023C, 0x5)
    Jump("loc_261")

    label("loc_247")

    OP_D2(0x70248, 0x70254, 0x5)
    Jump("loc_261")

    label("loc_254")

    OP_D2(0x270176, 0x270183, 0x5)
    Jump("loc_261")

    label("loc_261")

    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_6D(1900, 0, -54180, 0)
    OP_67(0, 6340, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(321, 0)
    SetChrPos(0x101, 550, 0, -54530, 0)
    SetChrPos(0x102, 1790, 0, -54700, 0)
    SetChrPos(0x10B, 200, 0, -55930, 0)
    SetChrPos(0xF9, 1610, 0, -56100, 0)
    OP_0D()
    OP_22(0x77, 0x0, 0x64)
    OP_22(0x135, 0x1, 0x32)
    Sleep(100)
    OP_24(0x135, 0x3C)
    Sleep(100)
    OP_24(0x135, 0x46)
    Sleep(100)
    OP_24(0x135, 0x50)
    Sleep(100)
    OP_24(0x135, 0x5A)
    Sleep(100)
    OP_24(0x135, 0x64)
    Sleep(300)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_3A8():
        OP_6D(3330, 0, -53050, 5500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3A8)

    def lambda_3C0():
        OP_67(0, 5530, -10000, 5500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C0)

    def lambda_3D8():
        OP_6B(4500, 5500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3D8)
    SetChrPos(0x8, -11850, 3000, -61530, 180)
    SetChrPos(0x9, 11620, 3000, -62560, 180)
    SetChrPos(0xA, 2009, 3000, -43000, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_43(0x8, 0x0, 0x0, 0x3)
    OP_43(0x9, 0x0, 0x0, 0x4)
    OP_43(0xA, 0x0, 0x0, 0x5)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 2)
    SetChrSubChip(0x101, 0)
    Sleep(100)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x102, 3)
    SetChrSubChip(0x102, 0)
    Sleep(100)

    def lambda_467():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_467)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x10B, 4)
    SetChrSubChip(0x10B, 0)
    Sleep(100)

    def lambda_489():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_489)
    SetChrChipByIndex(0xF9, 5)
    SetChrSubChip(0xF9, 0)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x9, 0x0)
    WaitChrThread(0xA, 0x0)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    def lambda_4BA():
        OP_6D(2280, 0, -53910, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4BA)

    def lambda_4D2():
        OP_67(0, 6120, -10000, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4D2)

    def lambda_4EA():
        OP_6B(3100, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4EA)

    def lambda_4FA():
        OP_8E(0xFE, 0x49C, 0x5DC, 0xFFFF1E56, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_4FA)
    Sleep(50)

    def lambda_51A():
        OP_8E(0xFE, 0x28, 0x5DC, 0xFFFF2CC0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_51A)
    Sleep(20)

    def lambda_53A():
        OP_8E(0xFE, 0xC30, 0x5DC, 0xFFFF3152, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_53A)
    WaitChrThread(0x101, 0x1)
    OP_44(0x8, 0x0)
    OP_44(0x9, 0x0)
    OP_44(0xA, 0x0)
    Battle(0x433, 0x0, 0x1, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_581"),
        (0, "loc_586"),
        (2, "loc_58D"),
        (SWITCH_DEFAULT, "loc_594"),
    )


    label("loc_581")

    OP_B4(0x0)
    Jump("loc_594")

    label("loc_586")

    Call(0, 6)
    Jump("loc_594")

    label("loc_58D")

    Call(0, 7)
    Jump("loc_594")

    label("loc_594")

    Return()

    # Function_2_1AF end

    def Function_3_595(): pass

    label("Function_3_595")

    OP_97(0xFE, 0xFFFFF394, 0xFFFF2158, 0x2AB98, 0x1F40, 0x1)
    OP_8C(0xFE, 225, 200)

    def lambda_5B7():

        label("loc_5B7")

        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        OP_48()
        Jump("loc_5B7")

    QueueWorkItem2(0xFE, 1, lambda_5B7)
    Return()

    # Function_3_595 end

    def Function_4_5C5(): pass

    label("Function_4_5C5")

    OP_97(0xFE, 0xFD2, 0xFFFF234C, 0x29810, 0x1F40, 0x1)
    OP_8C(0xFE, 135, 200)

    def lambda_5E7():

        label("loc_5E7")

        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        OP_48()
        Jump("loc_5E7")

    QueueWorkItem2(0xFE, 1, lambda_5E7)
    Return()

    # Function_4_5C5 end

    def Function_5_5F5(): pass

    label("Function_5_5F5")

    OP_97(0xFE, 0x5AA, 0xFFFF2F04, 0x2D2A8, 0x1F40, 0x1)
    OP_8C(0xFE, 0, 200)

    def lambda_617():

        label("loc_617")

        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        OP_48()
        Jump("loc_617")

    QueueWorkItem2(0xFE, 1, lambda_617)
    Return()

    # Function_5_5F5 end

    def Function_6_625(): pass

    label("Function_6_625")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x8, 0x0)
    OP_44(0x9, 0x0)
    OP_44(0xA, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    OP_6D(1110, 0, -55250, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 1110, 0, -55250, 0)
    SetChrPos(0x1, 1110, 0, -55250, 0)
    SetChrPos(0x2, 1110, 0, -55250, 0)
    SetChrPos(0x3, 1110, 0, -55250, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x10B, 65535)
    SetChrSubChip(0x10B, 0)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0xF9, 0)
    OP_A2(0x2224)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_6_625 end

    def Function_7_709(): pass

    label("Function_7_709")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x8, 0x0)
    OP_44(0x9, 0x0)
    OP_44(0xA, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    OP_6D(1110, 0, -57250, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 1110, 0, -57250, 180)
    SetChrPos(0x1, 1110, 0, -57250, 180)
    SetChrPos(0x2, 1110, 0, -57250, 180)
    SetChrPos(0x3, 1110, 0, -57250, 180)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x10B, 65535)
    SetChrSubChip(0x10B, 0)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0xF9, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_7_709 end

    def Function_8_7EA(): pass

    label("Function_8_7EA")

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
        (0, "loc_863"),
        (1, "loc_869"),
        (SWITCH_DEFAULT, "loc_86F"),
    )


    label("loc_863")

    OP_A2(0x1200)
    Jump("loc_86F")

    label("loc_869")

    OP_A2(0x1201)
    Jump("loc_86F")

    label("loc_86F")

    Return()

    # Function_8_7EA end

    def Function_9_870(): pass

    label("Function_9_870")

    FadeToDark(0, 0, -1)
    OP_6D(-107890, 0, -346700, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xA, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_9_870 end

    SaveToFile()

Try(main)
