from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C0600   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0600.x',
        MapIndex            = 20,
        MapDefaultBGM       = "ed60031",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/C0600_1 ._SN',
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
        'Mouki',                                # 9
        'Mouki',                                # 10
        'Mouki',                                # 11
        'Targeting Camera',                     # 12
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
        'ED6_DT29/CH12120 ._CH',             # 00
        'ED6_DT29/CH12121 ._CH',             # 01
        'ED6_DT27/CH04000 ._CH',             # 02
        'ED6_DT07/CH00120 ._CH',             # 03
        'ED6_DT07/CH00130 ._CH',             # 04
        'ED6_DT07/CH00140 ._CH',             # 05
        'ED6_DT07/CH00150 ._CH',             # 06
        'ED6_DT07/CH00160 ._CH',             # 07
        'ED6_DT07/CH00170 ._CH',             # 08
        'ED6_DT27/CH03005 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT29/CH12120P._CP',             # 00
        'ED6_DT29/CH12121P._CP',             # 01
        'ED6_DT27/CH04000P._CP',             # 02
        'ED6_DT07/CH00120P._CP',             # 03
        'ED6_DT07/CH00130P._CP',             # 04
        'ED6_DT07/CH00140P._CP',             # 05
        'ED6_DT07/CH00150P._CP',             # 06
        'ED6_DT07/CH00160P._CP',             # 07
        'ED6_DT07/CH00170P._CP',             # 08
        'ED6_DT27/CH03005P._CP',             # 09
    )

    DeclNpc(
        X                   = 0,
        Z                   = 6000,
        Y                   = -4059,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1100,
        Z                   = 6000,
        Y                   = -3020,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1100,
        Z                   = 6000,
        Y                   = -3020,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -32900,
        TriggerZ            = 0,
        TriggerY            = 84900,
        TriggerRange        = 1700,
        ActorX              = -32900,
        ActorZ              = 2500,
        ActorY              = 84900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -13900,
        TriggerZ            = 0,
        TriggerY            = 73100,
        TriggerRange        = 1700,
        ActorX              = -13900,
        ActorZ              = 2500,
        ActorY              = 73100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 2320,
        TriggerZ            = 0,
        TriggerY            = -360,
        TriggerRange        = 600,
        ActorX              = 2320,
        ActorZ              = 800,
        ActorY              = -360,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 1,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1E6",          # 00, 0
        "Function_1_207",          # 01, 1
        "Function_2_29E",          # 02, 2
        "Function_3_41B",          # 03, 3
        "Function_4_587",          # 04, 4
    )


    def Function_0_1E6(): pass

    label("Function_0_1E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x1, 0x80)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_206")
    Event(1, 0)

    label("loc_206")

    Return()

    # Function_0_1E6 end

    def Function_1_207(): pass

    label("Function_1_207")

    OP_72(0x0, 0x28)
    OP_72(0x1, 0x28)
    OP_72(0x2, 0x28)
    OP_72(0x3, 0x28)
    OP_72(0x4, 0x28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_235")
    OP_6F(0x0, 120)
    OP_6F(0x1, 60)

    label("loc_235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_24A")
    OP_6F(0x0, 120)
    OP_6F(0x1, 160)

    label("loc_24A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_25F")
    OP_6F(0x3, 120)
    OP_6F(0x4, 60)

    label("loc_25F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_274")
    OP_6F(0x2, 120)
    OP_6F(0x4, 160)

    label("loc_274")

    OP_64(0x2, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x1, 0x4000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x1, 0x100)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_298")
    OP_65(0x2, 0x1)

    label("loc_298")

    OP_22(0x1CD, 0x1, 0x64)
    Return()

    # Function_1_207 end

    def Function_2_29E(): pass

    label("Function_2_29E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C3")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_405")

    label("loc_2C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DC")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_405")

    label("loc_2DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F5")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_405")

    label("loc_2F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30E")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_405")

    label("loc_30E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_327")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_405")

    label("loc_327")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_340")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_405")

    label("loc_340")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_359")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_405")

    label("loc_359")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_372")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_405")

    label("loc_372")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38B")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_405")

    label("loc_38B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A4")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_405")

    label("loc_3A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BD")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_405")

    label("loc_3BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D6")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_405")

    label("loc_3D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EF")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_405")

    label("loc_3EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_405")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_405")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_41A")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_405")

    label("loc_41A")

    Return()

    # Function_2_29E end

    def Function_3_41B(): pass

    label("Function_3_41B")

    TalkBegin(0xFF)
    ClearMapFlags(0x1)

    AnonymousTalk(    #0
        "There is a lever. Move it?\x02",
    )

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FD")

    Menu(
        0,
        260,
        200,
        0,
        (
            "Drop To The Right\x01",      # 0
            "Drop To The Left\x01",       # 1
            "Don't Move\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B0")
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3C)
    OP_73(0x1)
    OP_A2(0x1)
    Jump("loc_4D1")

    label("loc_4B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D1")
    OP_6F(0x1, 100)
    OP_70(0x1, 0xA0)
    OP_73(0x1)
    OP_A2(0x0)

    label("loc_4D1")

    OP_6D(-32340, -60, 91590, 500)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x78)
    OP_73(0x0)
    OP_69(0x0, 0x258)
    Jump("loc_57E")

    label("loc_4FD")


    Menu(
        0,
        260,
        200,
        0,
        (
            "Return To Original Position\x01",      # 0
            "Don't Move\x01",                       # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_559")
    OP_6F(0x1, 0)
    OP_73(0x1)
    OP_A3(0x1)
    Jump("loc_56D")

    label("loc_559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_56D")
    OP_6F(0x1, 0)
    OP_73(0x1)
    OP_A3(0x0)

    label("loc_56D")

    OP_6F(0x0, 120)
    OP_70(0x0, 0x0)
    OP_73(0x0)

    label("loc_57E")

    SetMapFlags(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_3_41B end

    def Function_4_587(): pass

    label("Function_4_587")

    TalkBegin(0xFF)

    AnonymousTalk(    #1
        "There is a lever. Move it?\x02",
    )

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_664")

    Menu(
        0,
        260,
        200,
        0,
        (
            "Drop To The Right\x01",      # 0
            "Drop To The Left\x01",       # 1
            "Don't Move\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_628")
    OP_6F(0x4, 0)
    OP_70(0x4, 0x3C)
    OP_73(0x4)
    OP_A2(0x3)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x78)
    OP_73(0x3)
    Jump("loc_65A")

    label("loc_628")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65A")
    OP_6F(0x4, 100)
    OP_70(0x4, 0xA0)
    OP_73(0x4)
    OP_A2(0x2)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x78)
    OP_73(0x2)

    label("loc_65A")

    OP_69(0x0, 0x258)
    Jump("loc_6F6")

    label("loc_664")


    Menu(
        0,
        260,
        200,
        0,
        (
            "Return To Original Position\x01",      # 0
            "Don't Move\x01",                       # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_6D1")
    OP_6F(0x4, 0)
    OP_73(0x4)
    OP_6F(0x3, 120)
    OP_70(0x3, 0x0)
    OP_73(0x3)
    OP_A3(0x3)
    Jump("loc_6F6")

    label("loc_6D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_6F6")
    OP_6F(0x4, 0)
    OP_73(0x4)
    OP_6F(0x2, 120)
    OP_70(0x2, 0x0)
    OP_73(0x2)
    OP_A3(0x2)

    label("loc_6F6")

    TalkEnd(0xFF)
    Return()

    # Function_4_587 end

    SaveToFile()

Try(main)
