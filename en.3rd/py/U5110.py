from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U5110   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U5110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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
        'Plate',                                # 9
        'Plate',                                # 10
        'Plate',                                # 11
        'Bottle',                               # 12
        'Bottle',                               # 13
        'Fork',                                 # 14
        'Knife',                                # 15
        'Empty Glass',                          # 16
        'Gilbert',                              # 17
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
        'ED6_DT06/CH20020 ._CH',             # 00
        'ED6_DT06/CH20021 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT06/CH20020P._CP',             # 00
        'ED6_DT06/CH20021P._CP',             # 01
    )

    DeclNpc(
        X                   = 18160,
        Z                   = 800,
        Y                   = 11100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65536,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 18670,
        Z                   = 800,
        Y                   = 12140,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65536,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 18200,
        Z                   = 800,
        Y                   = 11940,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65536,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 17600,
        Z                   = 800,
        Y                   = 12140,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835008,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 17900,
        Z                   = 800,
        Y                   = 11800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835008,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 17600,
        Z                   = 800,
        Y                   = 11180,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 917504,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 18470,
        Z                   = 800,
        Y                   = 11100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 851968,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 18350,
        Z                   = 800,
        Y                   = 11550,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65537,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 112000,
        Z                   = 0,
        Y                   = -3670,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 112600,
        Y                   = 0,
        Z                   = 1000,
        Range               = 115170,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x7D0,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )


    DeclActor(
        TriggerX            = 21010,
        TriggerZ            = 0,
        TriggerY            = 15470,
        TriggerRange        = 1000,
        ActorX              = 21010,
        ActorZ              = 2000,
        ActorY              = 15470,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 86740,
        TriggerZ            = 0,
        TriggerY            = 41680,
        TriggerRange        = 1000,
        ActorX              = 86740,
        ActorZ              = 1000,
        ActorY              = 41680,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 139740,
        TriggerZ            = 0,
        TriggerY            = 41770,
        TriggerRange        = 1000,
        ActorX              = 139740,
        ActorZ              = 1000,
        ActorY              = 41770,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 115250,
        TriggerZ            = 0,
        TriggerY            = -34470,
        TriggerRange        = 1000,
        ActorX              = 115250,
        ActorZ              = 1000,
        ActorY              = -34470,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 142700,
        TriggerZ            = 0,
        TriggerY            = -34000,
        TriggerRange        = 1000,
        ActorX              = 142700,
        ActorZ              = 1000,
        ActorY              = -34000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2AE",          # 00, 0
        "Function_1_31E",          # 01, 1
        "Function_2_394",          # 02, 2
        "Function_3_557",          # 03, 3
        "Function_4_6A9",          # 04, 4
        "Function_5_7D5",          # 05, 5
        "Function_6_90C",          # 06, 6
        "Function_7_B8E",          # 07, 7
        "Function_8_E58",          # 08, 8
        "Function_9_E8A",          # 09, 9
        "Function_10_EE4",         # 0A, 10
        "Function_11_109D",        # 0B, 11
        "Function_12_11D3",        # 0C, 12
        "Function_13_127E",        # 0D, 13
    )


    def Function_0_2AE(): pass

    label("Function_0_2AE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F2")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_9F(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_2F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31D")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (116, "loc_30A"),
        (SWITCH_DEFAULT, "loc_31D"),
    )


    label("loc_30A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_END)), "loc_31A")
    SetMapFlags(0x10000000)
    Event(0, 13)

    label("loc_31A")

    Jump("loc_31D")

    label("loc_31D")

    Return()

    # Function_0_2AE end

    def Function_1_31E(): pass

    label("Function_1_31E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32F")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x83, 0x0)

    label("loc_32F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_341")
    OP_6F(0x1C, 0)
    Jump("loc_348")

    label("loc_341")

    OP_6F(0x1C, 60)

    label("loc_348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35A")
    OP_6F(0x1D, 0)
    Jump("loc_361")

    label("loc_35A")

    OP_6F(0x1D, 60)

    label("loc_361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_373")
    OP_6F(0x1E, 0)
    Jump("loc_37A")

    label("loc_373")

    OP_6F(0x1E, 60)

    label("loc_37A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38C")
    OP_6F(0x1F, 0)
    Jump("loc_393")

    label("loc_38C")

    OP_6F(0x1F, 60)

    label("loc_393")

    Return()

    # Function_1_31E end

    def Function_2_394(): pass

    label("Function_2_394")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1C, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2D9, 1)"), scpexpr(EXPR_END)), "loc_402")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\xD9\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2998)
    Jump("loc_46A")

    label("loc_402")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\xD9\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xD9\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1C, 60)
    OP_70(0x1C, 0x0)

    label("loc_46A")

    Jump("loc_549")

    label("loc_46D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05(6/12) [50 years later...] The 'Dangling Health-o-tron' swung limply in\x01",
            "Hideko's house, forgotten and neglected. It had been purchased 50 years\x01",
            "before, purely on Sato's recommendation.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x141, 0x0)

    label("loc_549")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_394 end

    def Function_3_557(): pass

    label("Function_3_557")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_630")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1D, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x29C, 1)"), scpexpr(EXPR_END)), "loc_5C5")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\x9C\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2999)
    Jump("loc_62D")

    label("loc_5C5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\x9C\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x9C\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1D, 60)
    OP_70(0x1D, 0x0)

    label("loc_62D")

    Jump("loc_69B")

    label("loc_630")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05Mr. Tiddles looks up with an annoyed expression. You disturbed his nap.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x142, 0x0)

    label("loc_69B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_557 end

    def Function_4_6A9(): pass

    label("Function_4_6A9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_782")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1E, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x18C, 1)"), scpexpr(EXPR_END)), "loc_717")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05Found \x1F\x8C\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x299A)
    Jump("loc_77F")

    label("loc_717")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05Found \x1F\x8C\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x8C\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1E, 60)
    OP_70(0x1E, 0x0)

    label("loc_77F")

    Jump("loc_7C7")

    label("loc_782")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05(Will write flavor text for food)\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x143, 0x0)

    label("loc_7C7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_6A9 end

    def Function_5_7D5(): pass

    label("Function_5_7D5")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1F, 0x1E)
    OP_73(0x1F)
    OP_6F(0x1F, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_3E(0x1EC, 1)

    AnonymousTalk(    #9
        "\x07\x05Found \x1F\xEC\x01\x07\x05.\x02",
    )

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_89E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x28)"), scpexpr(EXPR_END)), "loc_840")
    Jump("loc_89E")

    label("loc_840")

    CloseMessageWindow()

    AnonymousTalk(    #10
        "\x07\x05A recipe was written on a scrap of paper within.\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #11
        "\x07\x05Learned the recipe for \x1F\xEC\x01\x07\x05.\x02",
    )


    label("loc_89E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x299B)
    Jump("loc_8F5")

    label("loc_8B0")


    AnonymousTalk(    #12
        "\x07\x05Empty? No, my friend. I'm filled with artisan-style voidness.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_8F5")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x144, 0x0)
    Return()

    # Function_5_7D5 end

    def Function_6_90C(): pass

    label("Function_6_90C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9DB")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(2816)
    Sleep(500)
    Jump("loc_9DE")

    label("loc_9DB")

    TalkBegin(0xFF)

    label("loc_9DE")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #13
        "\x07\x05Select an Option\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A1A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B5D")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Restore HP/EP\x01",          # 0
            "Shop\x01",                   # 1
            "Synthesize Quartz\x01",      # 2
            "End\x01",                    # 3
        )
    )

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A76"),
        (1, "loc_AF1"),
        (2, "loc_B1F"),
        (SWITCH_DEFAULT, "loc_B4D"),
    )


    label("loc_A76")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xDD)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B5A")

    label("loc_AF1")

    OP_A9(0x1E)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #14
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_B5A")

    label("loc_B1F")

    OP_A9(0x6)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #15
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_B5A")

    label("loc_B4D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B5A")

    label("loc_B5A")

    Jump("loc_A1A")

    label("loc_B5D")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B8A")
    OP_A2(0x258E)
    EventEnd(0x1)
    Jump("loc_B8D")

    label("loc_B8A")

    TalkEnd(0xFF)

    label("loc_B8D")

    Return()

    # Function_6_90C end

    def Function_7_B8E(): pass

    label("Function_7_B8E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B9E")
    Return()

    label("loc_B9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA7")
    Return()

    label("loc_BA7")

    EventBegin(0x1)
    OP_8C(0x0, 174, 500)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #16
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE0")
    OP_A2(0x0)

    NpcTalk(    #17
        0x18,
        "Gilbert's Voice",
        (
            "#5P#40W*chomp* *chomp* *chomp*\x01",
            "Hmph... *munch* *munch*\x02\x03",

            "Why would I...*munch*...ever want\x01",
            "to be helped by THOSE losers? *munch*\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x18, 0x1, 0x0, 0x8)

    NpcTalk(    #18
        0x18,
        "Gilbert's Voice",
        (
            "#5P#60WGuh!#500W \x01",
            "#40WGraaaaaah!#500W\x01",
            "#20W*sound of banging on chest*\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #19
        0x18,
        "Gilbert's Voice",
        "#5P#4SAaaaaaah!\x02",
    )

    OP_7C(0x12C, 0x12C, 0xBB8, 0x12C)
    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #20
        0x18,
        "Gilbert's Voice",
        "#5P#40W...I-I thought I was gonna die...\x02",
    )

    CloseMessageWindow()
    Sleep(800)

    NpcTalk(    #21
        0x18,
        "Gilbert's Voice",
        (
            "#5P#40W...Huh? What's this...?\x01",
            "Sweat's coming from my eyes...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E3C")

    label("loc_DE0")


    NpcTalk(    #22
        0x18,
        "Gilbert's Voice",
        (
            "#5P#40WI'm not crying! I'm not...\x02\x03",

            "*sniffle* *munch*\x01",
            "*sniffle* *munch*\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E3C")

    OP_90(0x0, 0x0, 0x0, 0x3E8, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_7_B8E end

    def Function_8_E58(): pass

    label("Function_8_E58")

    OP_7C(0x12C, 0x12C, 0xBB8, 0x64)
    Sleep(800)
    OP_7C(0x64, 0x64, 0xBB8, 0x1F4)
    Sleep(1000)
    OP_22(0x72, 0x0, 0x64)
    Return()

    # Function_8_E58 end

    def Function_9_E8A(): pass

    label("Function_9_E8A")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #23
        "\x07\x05Open the Door?\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    Return()

    # Function_9_E8A end

    def Function_10_EE4(): pass

    label("Function_10_EE4")

    TalkBegin(0xFF)
    OP_22(0x222, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x18, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F34")
    OP_28(0x18, 0x4, 0x2)
    OP_82(0x88, 0x2)
    PlayEffect(0x89, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_F34")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x05A voice resounds inside your head...\x02",
    )

    CloseMessageWindow()
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #25
        (
            "\x07\x0C\x18#2S#80WWelcome...\x02\x03",

            "Entrust your fate to the dice...\x01",
            "Whether that decision will lead to \x01",
            "fortune or disaster, only they know...\x01",
            "Present a die before me...\x02\x03",

            "Only then shall the door open...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x339, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1099")
    Sleep(500)
    OP_22(0x138, 0x0, 0x64)
    Sleep(2000)
    Call(0, 9)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1096")
    Call(0, 11)

    label("loc_1096")

    Jump("loc_1099")

    label("loc_1099")

    TalkEnd(0xFF)
    Return()

    # Function_10_EE4 end

    def Function_11_109D(): pass

    label("Function_11_109D")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x0, 115300, 0, 38890, 0)
    SetChrPos(0x1, 113750, 0, 38610, 0)
    SetChrPos(0x2, 115320, 0, 37500, 0)
    SetChrPos(0x3, 113600, 0, 37500, 0)
    OP_6D(114660, 0, 40150, 0)
    OP_67(0, 5390, -10000, 0)
    OP_6B(3670, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    PlayEffect(0x87, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x1B, 0)
    OP_70(0x1B, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x1B)
    Sleep(500)

    def lambda_1186():
        OP_6B(3100, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1186)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(3000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_E3(0x0, 0xF, 0, 0x0)
    NewScene("ED6_DT21/P9002   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_109D end

    def Function_12_11D3(): pass

    label("Function_12_11D3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, -16250, -38000, 52300, 0)
    SetChrPos(0x1, -17950, -38000, 52240, 0)
    SetChrPos(0x2, -16580, -38000, 50060, 0)
    SetChrPos(0x3, -18080, -38000, 50420, 0)
    OP_6D(-17350, -38000, 53300, 0)
    OP_67(0, 6320, -10000, 0)
    OP_6B(4630, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_12_11D3 end

    def Function_13_127E(): pass

    label("Function_13_127E")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("ED6_DT21/U5111   ._SN", 115, 0, 0)
    IdleLoop()
    Return()

    # Function_13_127E end

    SaveToFile()

Try(main)
