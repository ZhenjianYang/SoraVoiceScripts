from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M5510   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5510.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60232",
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
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
        'ED6_DT29/CH14750 ._CH',             # 00
        'ED6_DT29/CH14751 ._CH',             # 01
        'ED6_DT29/CH14530 ._CH',             # 02
        'ED6_DT29/CH14531 ._CH',             # 03
        'ED6_DT29/CH14540 ._CH',             # 04
        'ED6_DT29/CH14541 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT29/CH14750P._CP',             # 00
        'ED6_DT29/CH14751P._CP',             # 01
        'ED6_DT29/CH14530P._CP',             # 02
        'ED6_DT29/CH14531P._CP',             # 03
        'ED6_DT29/CH14540P._CP',             # 04
        'ED6_DT29/CH14541P._CP',             # 05
    )

    DeclMonster(
        X                   = 136980,
        Z                   = 0,
        Y                   = 99210,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x19D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 147910,
        Z                   = 0,
        Y                   = 60040,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x19D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 179040,
        Z                   = 0,
        Y                   = 21700,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x19E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 135820,
        Z                   = 0,
        Y                   = 58050,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x19D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 5610,
        Z                   = 0,
        Y                   = 50530,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x19D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 58800,
        TriggerZ            = 0,
        TriggerY            = 101310,
        TriggerRange        = 1000,
        ActorX              = 58800,
        ActorZ              = 1300,
        ActorY              = 101310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 180210,
        TriggerZ            = 0,
        TriggerY            = 112920,
        TriggerRange        = 1000,
        ActorX              = 180210,
        ActorZ              = 1300,
        ActorY              = 112920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 171410,
        TriggerZ            = 0,
        TriggerY            = 105910,
        TriggerRange        = 1000,
        ActorX              = 171410,
        ActorZ              = 1300,
        ActorY              = 105910,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 142390,
        TriggerZ            = 0,
        TriggerY            = 71330,
        TriggerRange        = 1000,
        ActorX              = 142390,
        ActorZ              = 1300,
        ActorY              = 71330,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 137450,
        TriggerZ            = 0,
        TriggerY            = 54510,
        TriggerRange        = 1000,
        ActorX              = 137450,
        ActorZ              = 1300,
        ActorY              = 54510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 75460,
        TriggerZ            = 0,
        TriggerY            = 71460,
        TriggerRange        = 1000,
        ActorX              = 75460,
        ActorZ              = 1300,
        ActorY              = 71460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 93350,
        TriggerZ            = 0,
        TriggerY            = 28360,
        TriggerRange        = 1000,
        ActorX              = 93350,
        ActorZ              = 1300,
        ActorY              = 28360,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 29760,
        TriggerZ            = 0,
        TriggerY            = 73880,
        TriggerRange        = 1000,
        ActorX              = 29760,
        ActorZ              = 1000,
        ActorY              = 73880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 61450,
        TriggerZ            = 0,
        TriggerY            = 26210,
        TriggerRange        = 1000,
        ActorX              = 61450,
        ActorZ              = 1300,
        ActorY              = 26210,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 101070,
        TriggerZ            = 0,
        TriggerY            = 126290,
        TriggerRange        = 1000,
        ActorX              = 101070,
        ActorZ              = 1000,
        ActorY              = 126290,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 130000,
        TriggerZ            = 0,
        TriggerY            = 67000,
        TriggerRange        = 1000,
        ActorX              = 130000,
        ActorZ              = 1000,
        ActorY              = 67000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2F2",          # 00, 0
        "Function_1_2F3",          # 01, 1
        "Function_2_75E",          # 02, 2
        "Function_3_8AD",          # 03, 3
        "Function_4_9F9",          # 04, 4
        "Function_5_B2B",          # 05, 5
        "Function_6_BC0",          # 06, 6
        "Function_7_C55",          # 07, 7
        "Function_8_CEA",          # 08, 8
        "Function_9_D7F",          # 09, 9
        "Function_10_E14",         # 0A, 10
        "Function_11_EA9",         # 0B, 11
        "Function_12_F3E",         # 0C, 12
        "Function_13_1002",        # 0D, 13
        "Function_14_1180",        # 0E, 14
    )


    def Function_0_2F2(): pass

    label("Function_0_2F2")

    Return()

    # Function_0_2F2 end

    def Function_1_2F3(): pass

    label("Function_1_2F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x530, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_305")
    OP_6F(0x2A, 0)
    Jump("loc_30C")

    label("loc_305")

    OP_6F(0x2A, 60)

    label("loc_30C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x539, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31E")
    OP_6F(0x28, 0)
    Jump("loc_325")

    label("loc_31E")

    OP_6F(0x28, 60)

    label("loc_325")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x539, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_337")
    OP_6F(0x29, 0)
    Jump("loc_33E")

    label("loc_337")

    OP_6F(0x29, 60)

    label("loc_33E")

    OP_64(0x2, 0x1)
    OP_64(0x4, 0x1)
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46B")
    OP_72(0x202D, 0x0)
    ExitThread()
    OP_72(0x82D, 0x0)
    ExitThread()
    OP_6F(0x2D, 0)
    OP_72(0x202E, 0x0)
    ExitThread()
    OP_72(0x82E, 0x0)
    ExitThread()
    OP_6F(0x2E, 0)
    OP_72(0x2030, 0x0)
    ExitThread()
    OP_72(0x830, 0x0)
    ExitThread()
    OP_6F(0x30, 0)
    OP_72(0x2032, 0x0)
    ExitThread()
    OP_72(0x832, 0x0)
    ExitThread()
    OP_6F(0x32, 0)
    OP_72(0x2033, 0x0)
    ExitThread()
    OP_72(0x833, 0x0)
    ExitThread()
    OP_6F(0x33, 0)
    OP_72(0x2037, 0x0)
    ExitThread()
    OP_72(0x837, 0x0)
    ExitThread()
    OP_6F(0x37, 15)
    OP_72(0x2038, 0x0)
    ExitThread()
    OP_72(0x838, 0x0)
    ExitThread()
    OP_6F(0x38, 15)
    OP_72(0x2039, 0x0)
    ExitThread()
    OP_72(0x839, 0x0)
    ExitThread()
    OP_6F(0x39, 15)
    OP_72(0x203A, 0x0)
    ExitThread()
    OP_72(0x83A, 0x0)
    ExitThread()
    OP_6F(0x3A, 15)
    OP_72(0x203B, 0x0)
    ExitThread()
    OP_72(0x83B, 0x0)
    ExitThread()
    OP_6F(0x3B, 15)
    OP_72(0x203C, 0x0)
    ExitThread()
    OP_72(0x83C, 0x0)
    ExitThread()
    OP_6F(0x3C, 15)
    OP_72(0x203D, 0x0)
    ExitThread()
    OP_72(0x83D, 0x0)
    ExitThread()
    OP_6F(0x3D, 15)
    OP_72(0x203E, 0x0)
    ExitThread()
    OP_72(0x83E, 0x0)
    ExitThread()
    OP_6F(0x3E, 15)
    OP_72(0x203F, 0x0)
    ExitThread()
    OP_72(0x83F, 0x0)
    ExitThread()
    OP_6F(0x3F, 15)
    OP_72(0x22B, 0x0)
    ExitThread()
    OP_72(0x22C, 0x0)
    ExitThread()
    Jump("loc_730")

    label("loc_46B")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CF")
    OP_72(0x202D, 0x0)
    ExitThread()
    OP_72(0x82D, 0x0)
    ExitThread()
    OP_6F(0x2D, 1)
    OP_72(0x202E, 0x0)
    ExitThread()
    OP_72(0x82E, 0x0)
    ExitThread()
    OP_6F(0x2E, 1)
    OP_72(0x2030, 0x0)
    ExitThread()
    OP_72(0x830, 0x0)
    ExitThread()
    OP_6F(0x30, 1)
    OP_72(0x2032, 0x0)
    ExitThread()
    OP_72(0x832, 0x0)
    ExitThread()
    OP_6F(0x32, 1)
    OP_72(0x2033, 0x0)
    ExitThread()
    OP_72(0x833, 0x0)
    ExitThread()
    OP_6F(0x33, 1)
    OP_72(0x2037, 0x0)
    ExitThread()
    OP_72(0x837, 0x0)
    ExitThread()
    OP_6F(0x37, 30)
    OP_70(0x37, 0x1E)
    OP_72(0x2039, 0x0)
    ExitThread()
    OP_72(0x839, 0x0)
    ExitThread()
    OP_6F(0x39, 30)
    OP_70(0x39, 0x1E)
    OP_72(0x203A, 0x0)
    ExitThread()
    OP_72(0x83A, 0x0)
    ExitThread()
    OP_6F(0x3A, 30)
    OP_70(0x3A, 0x1E)
    OP_72(0x203B, 0x0)
    ExitThread()
    OP_72(0x83B, 0x0)
    ExitThread()
    OP_6F(0x3B, 30)
    OP_70(0x3B, 0x1E)
    OP_72(0x2038, 0x0)
    ExitThread()
    OP_72(0x838, 0x0)
    ExitThread()
    OP_6F(0x38, 15)
    OP_70(0x38, 0xF)
    OP_72(0x203C, 0x0)
    ExitThread()
    OP_72(0x83C, 0x0)
    ExitThread()
    OP_6F(0x3C, 15)
    OP_70(0x3C, 0xF)
    OP_72(0x203D, 0x0)
    ExitThread()
    OP_72(0x83D, 0x0)
    ExitThread()
    OP_6F(0x3D, 15)
    OP_70(0x3D, 0xF)
    OP_72(0x203E, 0x0)
    ExitThread()
    OP_72(0x83E, 0x0)
    ExitThread()
    OP_6F(0x3E, 15)
    OP_70(0x3E, 0xF)
    OP_72(0x203F, 0x0)
    ExitThread()
    OP_72(0x83F, 0x0)
    ExitThread()
    OP_6F(0x3F, 15)
    OP_70(0x3F, 0xF)
    OP_71(0x22C, 0x0)
    ExitThread()
    OP_72(0x22B, 0x0)
    ExitThread()
    Jump("loc_730")

    label("loc_5CF")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_730")
    OP_72(0x202D, 0x0)
    ExitThread()
    OP_72(0x82D, 0x0)
    ExitThread()
    OP_6F(0x2D, 2)
    OP_72(0x202E, 0x0)
    ExitThread()
    OP_72(0x82E, 0x0)
    ExitThread()
    OP_6F(0x2E, 2)
    OP_72(0x2030, 0x0)
    ExitThread()
    OP_72(0x830, 0x0)
    ExitThread()
    OP_6F(0x30, 2)
    OP_72(0x2032, 0x0)
    ExitThread()
    OP_72(0x832, 0x0)
    ExitThread()
    OP_6F(0x32, 2)
    OP_72(0x2033, 0x0)
    ExitThread()
    OP_72(0x833, 0x0)
    ExitThread()
    OP_6F(0x33, 2)
    OP_72(0x2037, 0x0)
    ExitThread()
    OP_72(0x837, 0x0)
    ExitThread()
    OP_6F(0x37, 15)
    OP_70(0x37, 0xF)
    OP_72(0x2039, 0x0)
    ExitThread()
    OP_72(0x839, 0x0)
    ExitThread()
    OP_6F(0x39, 15)
    OP_70(0x39, 0xF)
    OP_72(0x203A, 0x0)
    ExitThread()
    OP_72(0x83A, 0x0)
    ExitThread()
    OP_6F(0x3A, 15)
    OP_70(0x39, 0xF)
    OP_72(0x203B, 0x0)
    ExitThread()
    OP_72(0x83B, 0x0)
    ExitThread()
    OP_6F(0x3B, 15)
    OP_70(0x3B, 0xF)
    OP_72(0x2038, 0x0)
    ExitThread()
    OP_72(0x838, 0x0)
    ExitThread()
    OP_6F(0x38, 30)
    OP_70(0x38, 0x1E)
    OP_72(0x203C, 0x0)
    ExitThread()
    OP_72(0x83C, 0x0)
    ExitThread()
    OP_6F(0x3C, 30)
    OP_70(0x3C, 0x1E)
    OP_72(0x203D, 0x0)
    ExitThread()
    OP_72(0x83D, 0x0)
    ExitThread()
    OP_6F(0x3D, 30)
    OP_70(0x3D, 0x1E)
    OP_72(0x203E, 0x0)
    ExitThread()
    OP_72(0x83E, 0x0)
    ExitThread()
    OP_6F(0x3E, 30)
    OP_70(0x3E, 0x1E)
    OP_72(0x203F, 0x0)
    ExitThread()
    OP_72(0x83F, 0x0)
    ExitThread()
    OP_6F(0x3F, 30)
    OP_70(0x3F, 0x1E)
    OP_72(0x22C, 0x0)
    ExitThread()
    OP_71(0x22B, 0x0)
    ExitThread()

    label("loc_730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52A, 3)), scpexpr(EXPR_END)), "loc_75D")
    OP_72(0x202F, 0x0)
    ExitThread()
    OP_72(0x82F, 0x0)
    ExitThread()
    OP_6F(0x2F, 1)
    OP_72(0x2031, 0x0)
    ExitThread()
    OP_72(0x831, 0x0)
    ExitThread()
    OP_6F(0x31, 60)

    label("loc_75D")

    Return()

    # Function_1_2F3 end

    def Function_2_75E(): pass

    label("Function_2_75E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x530, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_837")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2A, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x327, 1)"), scpexpr(EXPR_END)), "loc_7CC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x27\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2981)
    Jump("loc_834")

    label("loc_7CC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\x27\x03\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x27\x03\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2A, 60)
    OP_70(0x2A, 0x0)

    label("loc_834")

    Jump("loc_89F")

    label("loc_837")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05After cleaning the inside, you decide to polish the outside as well.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x83, 0x0)

    label("loc_89F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_75E end

    def Function_3_8AD(): pass

    label("Function_3_8AD")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x539, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_986")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x28, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x557, 1)"), scpexpr(EXPR_END)), "loc_91B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\x57\x05\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x29C9)
    Jump("loc_983")

    label("loc_91B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\x57\x05\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x57\x05\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x28, 60)
    OP_70(0x28, 0x0)

    label("loc_983")

    Jump("loc_9EB")

    label("loc_986")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05I should move to a palace. That way I could be a...court chester.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x84, 0x0)

    label("loc_9EB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_8AD end

    def Function_4_9F9(): pass

    label("Function_4_9F9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x539, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x29, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x205, 1)"), scpexpr(EXPR_END)), "loc_A67")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05Found \x1F\x05\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x29CA)
    Jump("loc_ACF")

    label("loc_A67")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05Found \x1F\x05\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x05\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x29, 60)
    OP_70(0x29, 0x0)

    label("loc_ACF")

    Jump("loc_B1D")

    label("loc_AD2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05Back for more items? What am I, a shop?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x85, 0x0)

    label("loc_B1D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_9F9 end

    def Function_5_B2B(): pass

    label("Function_5_B2B")

    EventBegin(0x1)
    Fade(500)
    OP_6D(59490, 0, 100960, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 58850, 0, 100530, 0)
    SetChrPos(0x1, 57480, 0, 100070, 45)
    SetChrPos(0x2, 59450, 0, 99650, 0)
    SetChrPos(0x3, 58220, 0, 99270, 0)
    OP_0D()
    Sleep(500)
    Call(0, 14)
    EventEnd(0x0)
    Return()

    # Function_5_B2B end

    def Function_6_BC0(): pass

    label("Function_6_BC0")

    EventBegin(0x1)
    Fade(500)
    OP_6D(179420, 0, 112620, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 179200, 0, 112930, 90)
    SetChrPos(0x1, 177910, 0, 112580, 90)
    SetChrPos(0x2, 178530, 0, 113990, 135)
    SetChrPos(0x3, 177170, 0, 113460, 90)
    OP_0D()
    Sleep(500)
    Call(0, 14)
    EventEnd(0x0)
    Return()

    # Function_6_BC0 end

    def Function_7_C55(): pass

    label("Function_7_C55")

    EventBegin(0x1)
    Fade(500)
    OP_6D(173820, 0, 106060, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 172210, 0, 105810, 270)
    SetChrPos(0x1, 172860, 0, 105040, 270)
    SetChrPos(0x2, 172960, 0, 106850, 225)
    SetChrPos(0x3, 173830, 0, 106080, 270)
    OP_0D()
    Sleep(500)
    Call(0, 14)
    EventEnd(0x0)
    Return()

    # Function_7_C55 end

    def Function_8_CEA(): pass

    label("Function_8_CEA")

    EventBegin(0x1)
    Fade(500)
    OP_6D(142920, 0, 72050, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 143160, 0, 71240, 270)
    SetChrPos(0x1, 144080, 0, 70690, 270)
    SetChrPos(0x2, 143790, 0, 72530, 225)
    SetChrPos(0x3, 144730, 0, 71880, 270)
    OP_0D()
    Sleep(500)
    Call(0, 14)
    EventEnd(0x0)
    Return()

    # Function_8_CEA end

    def Function_9_D7F(): pass

    label("Function_9_D7F")

    EventBegin(0x1)
    Fade(500)
    OP_6D(136590, 0, 57570, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 136700, 0, 54920, 135)
    SetChrPos(0x1, 135360, 0, 54720, 90)
    SetChrPos(0x2, 136840, 0, 56020, 180)
    SetChrPos(0x3, 135530, 0, 56010, 135)
    OP_0D()
    Sleep(500)
    Call(0, 14)
    EventEnd(0x0)
    Return()

    # Function_9_D7F end

    def Function_10_E14(): pass

    label("Function_10_E14")

    EventBegin(0x1)
    Fade(500)
    OP_6D(76380, 0, 72230, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 76090, 0, 71920, 225)
    SetChrPos(0x1, 77120, 0, 71710, 270)
    SetChrPos(0x2, 76440, 0, 73220, 225)
    SetChrPos(0x3, 77470, 0, 72880, 225)
    OP_0D()
    Sleep(500)
    Call(0, 14)
    EventEnd(0x0)
    Return()

    # Function_10_E14 end

    def Function_11_EA9(): pass

    label("Function_11_EA9")

    EventBegin(0x1)
    Fade(500)
    OP_6D(94010, 0, 27580, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 93250, 0, 27620, 0)
    SetChrPos(0x1, 91910, 0, 27060, 45)
    SetChrPos(0x2, 93470, 0, 26490, 0)
    SetChrPos(0x3, 92190, 0, 26000, 0)
    OP_0D()
    Sleep(500)
    Call(0, 14)
    EventEnd(0x0)
    Return()

    # Function_11_EA9 end

    def Function_12_F3E(): pass

    label("Function_12_F3E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x327, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB7")
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #9
        (
            "\x07\x05There's a slot to insert a card. \x01",
            "Some kind of ID seems to be needed.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Jump("loc_1001")

    label("loc_FB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC6")
    Call(0, 13)
    Jump("loc_1001")

    label("loc_FC6")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #10
        "\x07\x05The gate is already open.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)

    label("loc_1001")

    Return()

    # Function_12_F3E end

    def Function_13_1002(): pass

    label("Function_13_1002")

    EventBegin(0x0)
    Fade(500)
    OP_6D(62470, 0, 26170, 0)
    OP_67(0, 6700, -10000, 0)
    OP_6B(2820, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x109, 61410, 0, 25390, 0)
    SetChrPos(0x102, 60060, 0, 24750, 45)
    SetChrPos(0xF0, 62040, 0, 24290, 0)
    SetChrPos(0xF1, 60630, 0, 23750, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x9D, 0x0, 0x64)
    OP_6F(0x2F, 1)
    OP_70(0x2F, 0x1)
    Sleep(500)

    def lambda_10B8():
        OP_6D(60150, 750, 28390, 1500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_10B8)

    def lambda_10D0():
        OP_67(0, 5700, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_10D0)

    def lambda_10E8():
        OP_6B(3390, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_10E8)

    def lambda_10F8():
        OP_6C(33000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_10F8)
    WaitChrThread(0x0, 0x0)
    Sleep(500)
    OP_22(0x6B, 0x0, 0x64)
    OP_B0(0x31, 0x1E)
    OP_6F(0x31, 0)
    OP_70(0x31, 0x3C)
    OP_73(0x31)
    Sleep(500)
    Fade(500)
    OP_6D(61410, 0, 25390, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_A2(0x2953)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_13_1002 end

    def Function_14_1180(): pass

    label("Function_14_1180")

    OP_22(0x9C, 0x0, 0x64)
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1267")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_72(0x202D, 0x0)
    ExitThread()
    OP_72(0x82D, 0x0)
    ExitThread()
    OP_6F(0x2D, 1)
    OP_72(0x202E, 0x0)
    ExitThread()
    OP_72(0x82E, 0x0)
    ExitThread()
    OP_6F(0x2E, 1)
    OP_72(0x2030, 0x0)
    ExitThread()
    OP_72(0x830, 0x0)
    ExitThread()
    OP_6F(0x30, 1)
    OP_72(0x2032, 0x0)
    ExitThread()
    OP_72(0x832, 0x0)
    ExitThread()
    OP_6F(0x32, 1)
    OP_72(0x2033, 0x0)
    ExitThread()
    OP_72(0x833, 0x0)
    ExitThread()
    OP_6F(0x33, 1)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    OP_71(0x837, 0x0)
    ExitThread()
    OP_6F(0x37, 15)
    OP_70(0x37, 0x1E)
    OP_71(0x839, 0x0)
    ExitThread()
    OP_6F(0x39, 15)
    OP_70(0x39, 0x1E)
    OP_71(0x83A, 0x0)
    ExitThread()
    OP_6F(0x3A, 15)
    OP_70(0x3A, 0x1E)
    OP_71(0x83B, 0x0)
    ExitThread()
    OP_6F(0x3B, 15)
    OP_70(0x3B, 0x1E)
    OP_71(0x22C, 0x0)
    ExitThread()
    OP_72(0x22B, 0x0)
    ExitThread()
    Sleep(500)
    Jump("loc_14F0")

    label("loc_1267")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13AD")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_72(0x202D, 0x0)
    ExitThread()
    OP_72(0x82D, 0x0)
    ExitThread()
    OP_6F(0x2D, 2)
    OP_72(0x202E, 0x0)
    ExitThread()
    OP_72(0x82E, 0x0)
    ExitThread()
    OP_6F(0x2E, 2)
    OP_72(0x2030, 0x0)
    ExitThread()
    OP_72(0x830, 0x0)
    ExitThread()
    OP_6F(0x30, 2)
    OP_72(0x2032, 0x0)
    ExitThread()
    OP_72(0x832, 0x0)
    ExitThread()
    OP_6F(0x32, 2)
    OP_72(0x2033, 0x0)
    ExitThread()
    OP_72(0x833, 0x0)
    ExitThread()
    OP_6F(0x33, 2)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    OP_71(0x838, 0x0)
    ExitThread()
    OP_6F(0x38, 15)
    OP_70(0x38, 0x1E)
    OP_71(0x83C, 0x0)
    ExitThread()
    OP_6F(0x3C, 15)
    OP_70(0x3C, 0x1E)
    OP_71(0x83D, 0x0)
    ExitThread()
    OP_6F(0x3D, 15)
    OP_70(0x3D, 0x1E)
    OP_71(0x83E, 0x0)
    ExitThread()
    OP_6F(0x3E, 15)
    OP_70(0x3E, 0x1E)
    OP_71(0x83F, 0x0)
    ExitThread()
    OP_6F(0x3F, 15)
    OP_70(0x3F, 0x1E)
    OP_71(0x837, 0x0)
    ExitThread()
    OP_6F(0x37, 1)
    OP_70(0x37, 0xF)
    OP_71(0x839, 0x0)
    ExitThread()
    OP_6F(0x39, 1)
    OP_70(0x39, 0xF)
    OP_71(0x83A, 0x0)
    ExitThread()
    OP_6F(0x3A, 1)
    OP_70(0x3A, 0xF)
    OP_71(0x83B, 0x0)
    ExitThread()
    OP_6F(0x3B, 1)
    OP_70(0x3B, 0xF)
    OP_72(0x22C, 0x0)
    ExitThread()
    OP_71(0x22B, 0x0)
    ExitThread()
    Sleep(500)
    Jump("loc_14F0")

    label("loc_13AD")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14F0")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_72(0x202D, 0x0)
    ExitThread()
    OP_72(0x82D, 0x0)
    ExitThread()
    OP_6F(0x2D, 1)
    OP_72(0x202E, 0x0)
    ExitThread()
    OP_72(0x82E, 0x0)
    ExitThread()
    OP_6F(0x2E, 1)
    OP_72(0x2030, 0x0)
    ExitThread()
    OP_72(0x830, 0x0)
    ExitThread()
    OP_6F(0x30, 1)
    OP_72(0x2032, 0x0)
    ExitThread()
    OP_72(0x832, 0x0)
    ExitThread()
    OP_6F(0x32, 1)
    OP_72(0x2033, 0x0)
    ExitThread()
    OP_72(0x833, 0x0)
    ExitThread()
    OP_6F(0x33, 1)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    OP_71(0x837, 0x0)
    ExitThread()
    OP_6F(0x37, 15)
    OP_70(0x37, 0x1E)
    OP_71(0x839, 0x0)
    ExitThread()
    OP_6F(0x39, 15)
    OP_70(0x39, 0x1E)
    OP_71(0x83A, 0x0)
    ExitThread()
    OP_6F(0x3A, 15)
    OP_70(0x3A, 0x1E)
    OP_71(0x83B, 0x0)
    ExitThread()
    OP_6F(0x3B, 15)
    OP_70(0x3B, 0x1E)
    OP_71(0x838, 0x0)
    ExitThread()
    OP_6F(0x38, 1)
    OP_70(0x38, 0xF)
    OP_71(0x83C, 0x0)
    ExitThread()
    OP_6F(0x3C, 1)
    OP_70(0x3C, 0xF)
    OP_71(0x83D, 0x0)
    ExitThread()
    OP_6F(0x3D, 1)
    OP_70(0x3D, 0xF)
    OP_71(0x83E, 0x0)
    ExitThread()
    OP_6F(0x3E, 1)
    OP_70(0x3E, 0xF)
    OP_71(0x83F, 0x0)
    ExitThread()
    OP_6F(0x3F, 1)
    OP_70(0x3F, 0xF)
    OP_71(0x22C, 0x0)
    ExitThread()
    OP_72(0x22B, 0x0)
    ExitThread()
    Sleep(500)

    label("loc_14F0")

    Return()

    # Function_14_1180 end

    SaveToFile()

Try(main)
