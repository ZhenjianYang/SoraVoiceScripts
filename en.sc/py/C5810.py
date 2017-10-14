from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5810   ._SN',
        MapName             = 'Other',
        Location            = 'C5810.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60062",
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
        'Gospel',                               # 9
        'Don',                                  # 10
        'Kyle',                                 # 11
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
        'ED6_DT26/CH20425 ._CH',             # 00
        'ED6_DT26/CH20425 ._CH',             # 01
        'ED6_DT26/CH20425 ._CH',             # 02
        'ED6_DT26/CH20425 ._CH',             # 03
        'ED6_DT26/CH20425 ._CH',             # 04
        'ED6_DT26/CH20425 ._CH',             # 05
        'ED6_DT26/CH20425 ._CH',             # 06
        'ED6_DT26/CH20425 ._CH',             # 07
        'ED6_DT07/CH02110 ._CH',             # 08
        'ED6_DT07/CH02120 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT26/CH20425P._CP',             # 00
        'ED6_DT26/CH20425P._CP',             # 01
        'ED6_DT26/CH20425P._CP',             # 02
        'ED6_DT26/CH20425P._CP',             # 03
        'ED6_DT26/CH20425P._CP',             # 04
        'ED6_DT26/CH20425P._CP',             # 05
        'ED6_DT26/CH20425P._CP',             # 06
        'ED6_DT26/CH20425P._CP',             # 07
        'ED6_DT07/CH02110P._CP',             # 08
        'ED6_DT07/CH02120P._CP',             # 09
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x8,
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
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -2800,
        TriggerZ            = 500,
        TriggerY            = -67080,
        TriggerRange        = 1500,
        ActorX              = -2810,
        ActorZ              = 1500,
        ActorY              = -67700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2800,
        TriggerZ            = 500,
        TriggerY            = -67080,
        TriggerRange        = 1500,
        ActorX              = -2810,
        ActorZ              = 1500,
        ActorY              = -67700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -5970,
        TriggerZ            = 0,
        TriggerY            = 11030,
        TriggerRange        = 1500,
        ActorX              = -5970,
        ActorZ              = 1000,
        ActorY              = 11030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 67040,
        TriggerZ            = 0,
        TriggerY            = 9980,
        TriggerRange        = 1500,
        ActorX              = 67040,
        ActorZ              = 1000,
        ActorY              = 9980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 120000,
        TriggerZ            = 0,
        TriggerY            = -1980,
        TriggerRange        = 1500,
        ActorX              = 120000,
        ActorZ              = 1000,
        ActorY              = -1980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 8600,
        TriggerZ            = 0,
        TriggerY            = 4940,
        TriggerRange        = 1000,
        ActorX              = 9260,
        ActorZ              = 0,
        ActorY              = 4980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 8620,
        TriggerZ            = 0,
        TriggerY            = 1030,
        TriggerRange        = 1000,
        ActorX              = 9240,
        ActorZ              = 0,
        ActorY              = 980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 54100,
        TriggerZ            = 0,
        TriggerY            = 9100,
        TriggerRange        = 1000,
        ActorX              = 54100,
        ActorZ              = 0,
        ActorY              = 9710,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 120470,
        TriggerZ            = 0,
        TriggerY            = 2140,
        TriggerRange        = 1000,
        ActorX              = 119850,
        ActorZ              = 0,
        ActorY              = 2140,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -18540,
        TriggerZ            = 0,
        TriggerY            = -75000,
        TriggerRange        = 1000,
        ActorX              = -19160,
        ActorZ              = 0,
        ActorY              = -75000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -11080,
        TriggerZ            = 0,
        TriggerY            = -69510,
        TriggerRange        = 1000,
        ActorX              = -11080,
        ActorZ              = 0,
        ActorY              = -68940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -18390,
        TriggerZ            = 0,
        TriggerY            = -85010,
        TriggerRange        = 1500,
        ActorX              = -18390,
        ActorZ              = 1000,
        ActorY              = -85010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_30A",          # 00, 0
        "Function_1_30B",          # 01, 1
        "Function_2_3E2",          # 02, 2
        "Function_3_539",          # 03, 3
        "Function_4_65D",          # 04, 4
        "Function_5_79F",          # 05, 5
        "Function_6_8CF",          # 06, 6
        "Function_7_9FD",          # 07, 7
        "Function_8_B7F",          # 08, 8
        "Function_9_2B53",         # 09, 9
        "Function_10_3472",        # 0A, 10
        "Function_11_34F8",        # 0B, 11
        "Function_12_358B",        # 0C, 12
        "Function_13_3D14",        # 0D, 13
        "Function_14_42A0",        # 0E, 14
        "Function_15_43C0",        # 0F, 15
        "Function_16_4A19",        # 10, 16
        "Function_17_6489",        # 11, 17
        "Function_18_725F",        # 12, 18
        "Function_19_72B8",        # 13, 19
        "Function_20_7311",        # 14, 20
        "Function_21_7397",        # 15, 21
        "Function_22_7428",        # 16, 22
    )


    def Function_0_30A(): pass

    label("Function_0_30A")

    Return()

    # Function_0_30A end

    def Function_1_30B(): pass

    label("Function_1_30B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x461, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31D")
    OP_6F(0x0, 0)
    Jump("loc_324")

    label("loc_31D")

    OP_6F(0x0, 60)

    label("loc_324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x461, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_336")
    OP_6F(0x1, 0)
    Jump("loc_33D")

    label("loc_336")

    OP_6F(0x1, 60)

    label("loc_33D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x461, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34F")
    OP_6F(0x2, 0)
    Jump("loc_356")

    label("loc_34F")

    OP_6F(0x2, 60)

    label("loc_356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x462, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_368")
    OP_6F(0x3, 0)
    Jump("loc_36F")

    label("loc_368")

    OP_6F(0x3, 60)

    label("loc_36F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x462, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_381")
    OP_6F(0x4, 0)
    Jump("loc_388")

    label("loc_381")

    OP_6F(0x4, 60)

    label("loc_388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x462, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39A")
    OP_6F(0x5, 0)
    Jump("loc_3A1")

    label("loc_39A")

    OP_6F(0x5, 60)

    label("loc_3A1")

    OP_64(0x7, 0x1)
    OP_71(0x2, 0x0)
    OP_71(0x2, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BE")
    OP_64(0x1, 0x1)
    Jump("loc_3C2")

    label("loc_3BE")

    OP_64(0x0, 0x1)

    label("loc_3C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_3D3")
    OP_A3(0x10F0)
    Event(0, 16)
    Jump("loc_3E1")

    label("loc_3D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_3E1")
    OP_A3(0x10F1)
    Event(0, 17)

    label("loc_3E1")

    Return()

    # Function_1_30B end

    def Function_2_3E2(): pass

    label("Function_2_3E2")

    OP_EA(0x2, 0xB4, 0x1, 0x0)
    OP_EA(0x2, 0xC, 0x2, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x461, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BF")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_458")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xFF\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x230D)
    Jump("loc_4BC")

    label("loc_458")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xFF\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFF\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_4BC")

    Jump("loc_52B")

    label("loc_4BF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05Wow... You're the first human to ever take\x01",
            "something from me! I'm so excited!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_52B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_3E2 end

    def Function_3_539(): pass

    label("Function_3_539")

    OP_EA(0x2, 0xB5, 0x1, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x461, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E7")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x1E)
    OP_73(0x1)
    OP_6F(0x1, 30)
    AddSepith(0x1, 0x64)
    AddSepith(0x3, 0x64)
    AddSepith(0x5, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #3
        (
            "Found\x01",
            "#2C#57IWater Sepith x100\x01",
            "#59IWind Sepith x100\x01",
            "#60ISpace Sepith x100#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x230E)
    Jump("loc_64B")

    label("loc_5E7")


    AnonymousTalk(    #4
        (
            "\x07\x05Wenn ist das Nunst?ck git und Slotermeyer? Ja!\x01",
            "Beiherhund das Oder die Flipperwaldt gersput!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_64B")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_539 end

    def Function_4_65D(): pass

    label("Function_4_65D")

    OP_EA(0x2, 0xB6, 0x1, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x461, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_724")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x1E)
    OP_73(0x2)
    OP_6F(0x2, 30)
    AddSepith(0x0, 0x64)
    AddSepith(0x2, 0x64)
    AddSepith(0x4, 0x64)
    AddSepith(0x6, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #5
        (
            "Found\x01",
            "#2C#56IEarth Sepith x100\x01",
            "#58|Fire Sepith x100\x01",
            "#62Time Sepith x100\x01",
            "#61IMirage Sepith x100#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x230F)
    Jump("loc_78D")

    label("loc_724")


    AnonymousTalk(    #6
        (
            "\x07\x05Ahem! Two penguins walk into a bar...\x01",
            "which is stupid because the second one should have seen it.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_78D")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_65D end

    def Function_5_79F(): pass

    label("Function_5_79F")

    OP_EA(0x2, 0xB7, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x462, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_877")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_810")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "Found \x1F\xF7\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2310)
    Jump("loc_874")

    label("loc_810")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "Found \x1F\xF7\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF7\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_874")

    Jump("loc_8C1")

    label("loc_877")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05Empty. But THAT should come as no surprise.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_8C1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_79F end

    def Function_6_8CF(): pass

    label("Function_6_8CF")

    OP_EA(0x2, 0xB8, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x462, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A7")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2CC, 1)"), scpexpr(EXPR_END)), "loc_940")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "Found \x1F\xCC\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2311)
    Jump("loc_9A4")

    label("loc_940")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "Found \x1F\xCC\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xCC\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_9A4")

    Jump("loc_9EF")

    label("loc_9A7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x05You obtain...NOTHING! ABSOLUTELY NOTHING!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_9EF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_8CF end

    def Function_7_9FD(): pass

    label("Function_7_9FD")

    OP_EA(0x2, 0xB9, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x462, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x206, 1)"), scpexpr(EXPR_END)), "loc_A6E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #13
        "Found \x1F\x06\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2312)
    Jump("loc_AD2")

    label("loc_A6E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "Found \x1F\x06\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x06\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_AD2")

    Jump("loc_B71")

    label("loc_AD5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "\x07\x05Let's take all the typos we accidentally left in\x01",
            "this game at launch and shove them all in here.\x01",
            "Pretend they never happened.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B71")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_9FD end

    def Function_8_B7F(): pass

    label("Function_8_B7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BA2")
    Call(0, 10)
    Call(0, 11)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_BA2")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "\x07\x05#1SCradle 35 Municipal Office\x01",
            "* Access to services limited to citizens only.\x01",
            "* Due to communication interruptions with the\x01",
            "Axis Pillar, services may be temporarily\x01",
            "restricted.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B1E")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x0, 0x0, 0x28, 0x5A, 0x1)
    OP_CC(0x1, 0x0, "Database Access")
    OP_CC(0x1, 0x0, "Request Gospel Reprint")
    OP_CC(0x1, 0x0, "Quit")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CEA"),
        (1, "loc_1471"),
        (SWITCH_DEFAULT, "loc_2AFC"),
    )


    label("loc_CEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1461")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    AnonymousTalk(    #17 op#5
        (
            "\x07\x05#1SViewable data is currently limited.\x01",
            "Please select an option.\x05\x02",
        )
    )

    OP_CC(0x0, 0x1, 0x28, 0xBE, 0x1)
    OP_CC(0x1, 0x1, "Halo Rail")
    OP_CC(0x2, 0x1)
    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D77"),
        (SWITCH_DEFAULT, "loc_1451"),
    )


    label("loc_D77")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1441")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x0, 0x2, 0x28, 0xFA, 0x1)
    OP_CC(0x1, 0x2, "About the Halo Rail")
    OP_CC(0x1, 0x2, "About the Station Terminals")
    OP_CC(0x1, 0x2, "About Emergency Operations Mode")
    OP_CC(0x2, 0x2)
    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E13"),
        (1, "loc_104B"),
        (2, "loc_1228"),
        (SWITCH_DEFAULT, "loc_1431"),
    )


    label("loc_E13")


    AnonymousTalk(    #18
        (
            "\x07\x05#1SThe Halo Rail is a groundbreaking transit method\x01",
            "unique to the Liber Ark. Utilizing our powerful spatial\x01",
            "manipulation technology, the system projects force-field\x01",
            "rails as needed, removing all need for physical rails.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #19
        (
            "\x07\x05#1SPerhaps the greatest advantage of this system is the total\x01",
            "lack of restriction on rail placement. It is possible to\x01",
            "flexibly connect every one of the city's countless stations\x01",
            "directly. The Halo Rail helps carry all citizens to a\x01",
            "pleasant, fulfilling city life. Should you have business in\x01",
            "other sectors, be sure to make use of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_143E")

    label("loc_104B")


    AnonymousTalk(    #20
        (
            "\x07\x05#1SAll Halo Rail station terminals are capable of printing rail\x01",
            "passes, and offer a host of other services. Of these, the\x01",
            "Online Shop is noteworthy for providing various useful daily\x01",
            "items, as well as offering many sorts of tickets and passes.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #21
        (
            "\x07\x05#1SFurthermore, in the case that the Halo Rail main service is\x01",
            "inoperative for some reason, users may also engage the\x01",
            "station in Emergency Operations Mode, as well as open\x01",
            "emergency substratum passages at all terminals.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_143E")

    label("loc_1228")


    AnonymousTalk(    #22
        (
            "\x07\x05#1SEmergency Operations Mode is, as the name implies, the\x01",
            "emergency last-ditch operation mode for the Halo Rail\x01",
            "service. Should an emergency arise in which power from the\x01",
            "Axis Pillar is cut to the Halo Rail, this mode switches the\x01",
            "rail to local backup, allowing for semi-normal operation on\x01",
            "a temporary basis.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #23
        (
            "\x07\x05#1SAs this mode is operated on a station-by-station basis,\x01",
            "should multiple stations suffer power cuts, Emergency\x01",
            "Operations Mode must be enabled at each station or they will\x01",
            "not be able to connect.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_143E")

    label("loc_1431")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_143E")

    label("loc_143E")

    Jump("loc_D77")

    label("loc_1441")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_145E")

    label("loc_1451")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_145E")

    label("loc_145E")

    Jump("loc_CEA")

    label("loc_1461")

    OP_5F(0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2B1B")

    label("loc_1471")

    OP_A2(0x22D1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrName("")

    AnonymousTalk(    #24
        (
            "\x07\x05#1SDue to current communication errors with the Axis Pillar\x01",
            "central registrar, all re-issued Gospels will be temporary.\x01",
            "Please enter the name of the applicant for comparison to the\x01",
            "local database.\x02",
        )
    )

    CloseMessageWindow()
    OP_5F(0x0)
    OP_57(0x3C, 0xAA, 0x9, "Who will make the request?")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x0, 0x1, 0x55, 0x104, 0x0)
    OP_CC(0x1, 0x1, "Estelle")
    OP_CC(0x1, 0x1, "Joshua")
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_15DB"),
        (3, "loc_15EC"),
        (4, "loc_15FA"),
        (5, "loc_1605"),
        (6, "loc_1611"),
        (7, "loc_161C"),
        (8, "loc_1626"),
        (10, "loc_1632"),
        (SWITCH_DEFAULT, "loc_1640"),
    )


    label("loc_15DB")

    OP_CC(0x1, 0x1, "Scherazard")
    Jump("loc_1640")

    label("loc_15EC")

    OP_CC(0x1, 0x1, "Olivier")
    Jump("loc_1640")

    label("loc_15FA")

    OP_CC(0x1, 0x1, "Kloe")
    Jump("loc_1640")

    label("loc_1605")

    OP_CC(0x1, 0x1, "Agate")
    Jump("loc_1640")

    label("loc_1611")

    OP_CC(0x1, 0x1, "Tita")
    Jump("loc_1640")

    label("loc_161C")

    OP_CC(0x1, 0x1, "Zin")
    Jump("loc_1640")

    label("loc_1626")

    OP_CC(0x1, 0x1, "Kevin")
    Jump("loc_1640")

    label("loc_1632")

    OP_CC(0x1, 0x1, "Josette")
    Jump("loc_1640")

    label("loc_1640")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_1669"),
        (3, "loc_167A"),
        (4, "loc_1688"),
        (5, "loc_1693"),
        (6, "loc_169F"),
        (7, "loc_16AA"),
        (8, "loc_16B4"),
        (10, "loc_16C0"),
        (SWITCH_DEFAULT, "loc_16CE"),
    )


    label("loc_1669")

    OP_CC(0x1, 0x1, "Scherazard")
    Jump("loc_16CE")

    label("loc_167A")

    OP_CC(0x1, 0x1, "Olivier")
    Jump("loc_16CE")

    label("loc_1688")

    OP_CC(0x1, 0x1, "Kloe")
    Jump("loc_16CE")

    label("loc_1693")

    OP_CC(0x1, 0x1, "Agate")
    Jump("loc_16CE")

    label("loc_169F")

    OP_CC(0x1, 0x1, "Tita")
    Jump("loc_16CE")

    label("loc_16AA")

    OP_CC(0x1, 0x1, "Zin")
    Jump("loc_16CE")

    label("loc_16B4")

    OP_CC(0x1, 0x1, "Kevin")
    Jump("loc_16CE")

    label("loc_16C0")

    OP_CC(0x1, 0x1, "Josette")
    Jump("loc_16CE")

    label("loc_16CE")

    OP_CC(0x2, 0x1)
    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_16ED"),
        (1, "loc_16FA"),
        (2, "loc_1707"),
        (3, "loc_172B"),
        (SWITCH_DEFAULT, "loc_174F"),
    )


    label("loc_16ED")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_174F")

    label("loc_16FA")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_174F")

    label("loc_1707")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1728")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1728")

    Jump("loc_174F")

    label("loc_172B")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_174C")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_174C")

    Jump("loc_174F")

    label("loc_174F")

    OP_5F(0x1)
    OP_5F(0x2)
    OP_57(0x28, 0xAA, 0xB, "#2CPlease enter your name.")

    Menu(
        1,
        70,
        260,
        0,
        (
            "Ulrich\x01",        # 0
            "Georg\x01",         # 1
            "Elroy\x01",         # 2
            "Celeste\x01",       # 3
            "Edelhoff\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17BE")
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_17BE")

    OP_5F(0x1)

    Menu(
        1,
        110,
        260,
        0,
        (
            "A\x01",      # 0
            "B\x01",      # 1
            "C\x01",      # 2
            "D\x01",      # 3
            "E\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17EE")
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_17EE")

    OP_5F(0x1)

    Menu(
        1,
        65,
        260,
        0,
        (
            "Astray\x01",         # 0
            "Weissmann\x01",      # 1
            "Epstein\x01",        # 2
            "Auslese\x01",        # 3
            "Reinford\x01",       # 4
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_183E")
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_183E")

    OP_5F(0x1)
    OP_DA()
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    Fade(500)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(72, 320, 56, 3)
    EventBegin(0x0)
    OP_6D(-3670, 230, -66890, 0)
    OP_67(0, 5740, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_A2(0x3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_18C7"),
        (1, "loc_190E"),
        (2, "loc_1955"),
        (3, "loc_199C"),
        (SWITCH_DEFAULT, "loc_19E3"),
    )


    label("loc_18C7")

    SetChrPos(0x101, -2790, 500, -68180, 0)
    SetChrPos(0x102, -2680, 220, -69410, 0)
    SetChrPos(0xF8, -1230, 0, -69950, 315)
    SetChrPos(0xF9, -3450, 220, -69930, 0)
    Jump("loc_19E3")

    label("loc_190E")

    SetChrPos(0x102, -2790, 500, -68180, 0)
    SetChrPos(0x101, -2680, 220, -69410, 0)
    SetChrPos(0xF8, -1230, 0, -69950, 315)
    SetChrPos(0xF9, -3450, 220, -69930, 0)
    Jump("loc_19E3")

    label("loc_1955")

    SetChrPos(0xF8, -2790, 500, -68180, 0)
    SetChrPos(0x101, -2680, 220, -69410, 0)
    SetChrPos(0x102, -1230, 0, -69950, 315)
    SetChrPos(0xF9, -3450, 220, -69930, 0)
    Jump("loc_19E3")

    label("loc_199C")

    SetChrPos(0xF9, -2790, 500, -68180, 0)
    SetChrPos(0x101, -2680, 220, -69410, 0)
    SetChrPos(0x102, -1230, 0, -69950, 315)
    SetChrPos(0xF8, -3450, 220, -69930, 0)
    Jump("loc_19E3")

    label("loc_19E3")

    OP_0D()
    Sleep(200)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2064")
    SetChrName("Artificial Voice")

    AnonymousTalk(    #25
        (
            "\x07\x05Name - match found.\x01",
            "Bio pattern - 73% match to records.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #26
        "\x07\x05Applicant temporarily recognized as Celeste D. Auslese.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #27
        "\x07\x05Re-printing Gospel.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    LoadEffect(0x0, "map\\\\mp027_01.eff")
    PlayEffect(0x0, 0x0, 0x8, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x8, -2810, 2500, -67130, 0)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    OP_22(0x99, 0x0, 0x64)

    def lambda_1B20():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1B20)
    OP_91(0x8, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
    WaitChrThread(0x8, 0x1)
    OP_82(0x0, 0x2)
    Sleep(500)

    ChrTalk(    #28
        0x105,
        "#1164FOh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        "#1004FWhoa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        "#1042FLooks like spatial translocation.\x02",
    )

    CloseMessageWindow()
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    SetChrFlags(0x8, 0x80)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #31
        "\x07\x00Received #1039i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x40F, 1)
    OP_8C(0x105, 180, 400)

    ChrTalk(    #32
        0x105,
        (
            "#1160F#4PIt's...a real Gospel.\x01",
            "Just as they used in the ancient past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#1002FYeah. The society replicas are amazingly accurate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x102,
        (
            "#1040FSo we were right. The Celeste D. Auslese mentioned\x01",
            "in the towers was your ancestor, Kloe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x105,
        (
            "#1160F#4PThey must be.\x02\x03",

            "#1167FThey must have been the one who took\x01",
            "charge in leading people from the city.\x02\x03",

            "#1382FI'm a little surprised the computer thinks\x01",
            "we're so biologically similar, though...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E78")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as saw about Gospel at station terminal\x01",              # 0
            "Set as did not see about Gospel at station terminal\x01",      # 1
            "No change\x01",                                                # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E6C"),
        (1, "loc_1E72"),
        (SWITCH_DEFAULT, "loc_1E78"),
    )


    label("loc_1E6C")

    OP_A2(0x221A)
    Jump("loc_1E78")

    label("loc_1E72")

    OP_A3(0x221A)
    Jump("loc_1E78")

    label("loc_1E78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 2)), scpexpr(EXPR_END)), "loc_1F6D")

    ChrTalk(    #36
        0x101,
        (
            "#1001FHaha! As far as I'm concerned, it's\x01",
            "another one for 'divine providence'!\x02\x03",

            "#1006FAnyway, I bet we can open that underground\x01",
            "gate if we use this at the station terminal.\x02\x03",

            "Let's get going!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #37
        0x105,
        "#1161F#4PYes, absolutely.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2043")

    label("loc_1F6D")


    ChrTalk(    #38
        0x101,
        (
            "#1001FHaha! As far as I'm concerned, it's\x01",
            "another one for 'divine providence'!\x02\x03",

            "#1006FAnyway, I sure won't complain about having\x01",
            "a Gospel in our pocket.\x02\x03",

            "Let's take it with us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #39
        0x105,
        "#1168F#4PGood idea!\x02",
    )

    CloseMessageWindow()

    label("loc_2043")

    OP_A2(0x221B)
    OP_64(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_28(0x9D, 0x1, 0x800)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2B1B")

    label("loc_2064")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2408")
    SetChrName("Artificial Voice")
    SetMessageWindowPos(-1, 320, 56, 3)

    AnonymousTalk(    #40
        (
            "\x07\x05Bio pattern - match found in database.\x01",
            "Name - match error.\x01",
            "Please enter the correct name.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23F5")

    ChrTalk(    #41
        0x101,
        "#1004FWhat the heck?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x102,
        (
            "#1035FIt must be matching the name and biological\x01",
            "signature of the applicant with a database\x01",
            "of citizens.\x02\x03",

            "#1040FBut, wait.\x01",
            "If there's a biological match...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 180, 400)

    ChrTalk(    #43
        0x105,
        (
            "#1167F#4PYes, it seems to think I'm one\x01",
            "of my ancestors.\x02\x03",

            "#1162FIf only we knew their name!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#1002FThe name of Kloe's ancestors?\x02\x03",

            "#1015F(Wait, bell, ringing...)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 2)), scpexpr(EXPR_END)), "loc_2326")

    ChrTalk(    #45
        0x102,
        (
            "#1040FEither way, it's as the professor warned.\x01",
            "We need to know what happened here in\x01",
            "the past.\x02\x03",

            "Let's return to the Arseille and examine\x01",
            "the data decrypted by the Capel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23D8")

    label("loc_2326")


    ChrTalk(    #46
        0x102,
        (
            "#1040FOne way or another, this all seems pretty\x01",
            "advanced and probably a little over our\x01",
            "heads.\x02\x03",

            "It might be a good idea to go back and\x01",
            "talk to Professor Russell about this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23D8")

    OP_8C(0x105, 0, 400)
    OP_A2(0x0)
    SetMessageWindowPos(330, 68, 34, 12)
    SetChrName("")

    AnonymousTalk(    #47
        "\x07\x05\x02",
    )

    Jump("loc_2B1B")

    label("loc_23F5")

    SetMessageWindowPos(330, 68, 34, 12)
    SetChrName("")

    AnonymousTalk(    #48
        "\x07\x05\x02",
    )

    Jump("loc_2AF9")

    label("loc_2408")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_278C")
    SetChrName("Artificial Voice")

    AnonymousTalk(    #49
        (
            "\x07\x05Name - match found.\x01",
            "Bio pattern - error.\x01",
            "Bio pattern does not match.\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #50
        "\x07\x05Aborting Gospel print.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2779")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_24BD"),
        (1, "loc_24C0"),
        (2, "loc_24C3"),
        (3, "loc_24C6"),
        (SWITCH_DEFAULT, "loc_24C9"),
    )


    label("loc_24BD")

    Jump("loc_24C9")

    label("loc_24C0")

    Jump("loc_24C9")

    label("loc_24C3")

    Jump("loc_24C9")

    label("loc_24C6")

    Jump("loc_24C9")

    label("loc_24C9")


    ChrTalk(    #51
        0x101,
        "#1004FWhat the?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x102,
        (
            "#1035FIt must be matching the name and biological\x01",
            "signature of the applicant with a database of\x01",
            "citizens.\x02\x03",

            "#1043FWe had the name right, but the\x01",
            "biological pattern doesn't match.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1007FMmm, not sure what we can do\x01",
            "about that, then.\x02\x03",

            "#1015F(Though wait a minute. Auslese!)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 2)), scpexpr(EXPR_END)), "loc_26B1")

    ChrTalk(    #54
        0x102,
        (
            "#1040FEither way, it's as the professor warned.\x01",
            "We need to know what happened here in\x01",
            "the past.\x02\x03",

            "Let's return to the Arseille and examine\x01",
            "the data decrypted by the Capel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2763")

    label("loc_26B1")


    ChrTalk(    #55
        0x102,
        (
            "#1040FOne way or another, this all seems pretty\x01",
            "advanced and probably a little over our\x01",
            "heads.\x02\x03",

            "It might be a good idea to go back and\x01",
            "talk to Professor Russell about this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2763")

    OP_A2(0x1)
    SetMessageWindowPos(330, 68, 34, 12)
    SetChrName("")

    AnonymousTalk(    #56
        "\x07\x05\x02",
    )

    Jump("loc_2B1B")

    label("loc_2779")

    SetMessageWindowPos(330, 68, 34, 12)
    SetChrName("")

    AnonymousTalk(    #57
        "\x07\x05\x02",
    )

    Jump("loc_2AF9")

    label("loc_278C")

    SetChrName("Artificial Voice")

    AnonymousTalk(    #58
        (
            "\x07\x05Name - match error.\x01",
            "Bio pattern - not found in database.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #59
        "\x07\x05Aborting Gospel print.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AE9")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_281D"),
        (1, "loc_2820"),
        (2, "loc_2823"),
        (3, "loc_2826"),
        (SWITCH_DEFAULT, "loc_2829"),
    )


    label("loc_281D")

    Jump("loc_2829")

    label("loc_2820")

    Jump("loc_2829")

    label("loc_2823")

    Jump("loc_2829")

    label("loc_2826")

    Jump("loc_2829")

    label("loc_2829")


    ChrTalk(    #60
        0x101,
        "#1004FUh, what happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x102,
        (
            "#1035FIt must be matching the name and biological\x01",
            "signature of the applicant with a database of\x01",
            "citizens.\x02\x03",

            "#1042FUnless we somehow have both,\x01",
            "there's little we can do here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1019FUgh, great. So short of pulling a citizen out\x01",
            "of the past, we're not gonna get anywhere\x01",
            "with this.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 2)), scpexpr(EXPR_END)), "loc_2A21")

    ChrTalk(    #63
        0x102,
        (
            "#1040FEither way, it's as the professor warned.\x01",
            "We need to know what happened here in\x01",
            "the past.\x02\x03",

            "Let's return to the Arseille and examine\x01",
            "the data decrypted by the Capel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD3")

    label("loc_2A21")


    ChrTalk(    #64
        0x102,
        (
            "#1040FOne way or another, this all seems pretty\x01",
            "advanced and probably a little over our\x01",
            "heads.\x02\x03",

            "It might be a good idea to go back and\x01",
            "talk to Professor Russell about this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AD3")

    OP_A2(0x2)
    SetMessageWindowPos(330, 68, 34, 12)
    SetChrName("")

    AnonymousTalk(    #65
        "\x07\x05\x02",
    )

    Jump("loc_2B1B")

    label("loc_2AE9")

    SetMessageWindowPos(330, 68, 34, 12)
    SetChrName("")

    AnonymousTalk(    #66
        "\x07\x05\x02",
    )


    label("loc_2AF9")

    Jump("loc_2B1B")

    label("loc_2AFC")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2B1B")

    label("loc_2B1B")

    Jump("loc_C76")

    label("loc_2B1E")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2B4C")
    EventEnd(0x0)

    label("loc_2B4C")

    OP_A3(0x3)
    TalkEnd(0xFF)
    Return()

    # Function_8_B7F end

    def Function_9_2B53(): pass

    label("Function_9_2B53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B76")
    Call(0, 10)
    Call(0, 11)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_2B76")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #67
        (
            "\x07\x05#1SCradle #35 Municipal Office\x01",
            "* Access to services limited to citizens only.\x01",
            "* Due to communication interruptions with the\x01",
            "Axis Pillar, services may be temporarily\x01",
            "restricted.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C49")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3449")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x0, 0x0, 0x28, 0x64, 0x1)
    OP_CC(0x1, 0x0, "Database Access")
    OP_CC(0x1, 0x0, "Quit")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C99"),
        (0, "loc_2C99"),
        (SWITCH_DEFAULT, "loc_3427"),
    )


    label("loc_2C99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3417")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    AnonymousTalk(    #68
        (
            "\x07\x05#1SViewable data is currently limited.\x01",
            "Please select an option.\x02",
        )
    )

    CloseMessageWindow()
    OP_CC(0x0, 0x1, 0x28, 0xB4, 0x1)
    OP_CC(0x1, 0x1, "Halo Rail")
    OP_CC(0x2, 0x1)
    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2D26"),
        (SWITCH_DEFAULT, "loc_3407"),
    )


    label("loc_2D26")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33F7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x0, 0x2, 0x28, 0xF0, 0x1)
    OP_CC(0x1, 0x2, "About the Halo Rail")
    OP_CC(0x1, 0x2, "About the Station Terminals")
    OP_CC(0x1, 0x2, "About Emergency Operations Mode")
    OP_CC(0x2, 0x2)
    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2DC2"),
        (1, "loc_3002"),
        (2, "loc_31DE"),
        (SWITCH_DEFAULT, "loc_33E7"),
    )


    label("loc_2DC2")


    AnonymousTalk(    #69
        (
            "\x07\x05#1SThe Halo Rail is a unique, groundbreaking transit method\x01",
            "unique to the Liber Ark. Utilizing our powerful spatial\x01",
            "manipulation technology, the system projects force-field\x01",
            "rails as needed, removing all need for physical rails.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #70
        (
            "\x07\x05#1SPerhaps the greatest advantage of this system is the total\x01",
            "lack of restriction on rail placement. It is possible to\x01",
            "flexibly connect every one of the city's countless stations\x01",
            "directly. The Halo Rail helps carry all citizens to a\x01",
            "pleasant, fulfilling city life. Should you have business in\x01",
            "other sectors, be sure to make use of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33F4")

    label("loc_3002")


    AnonymousTalk(    #71
        (
            "\x07\x05#1SAll Halo Rail station terminals are capable of printing rail\x01",
            "passes, and offer a host of other services. Of these, the\x01",
            "Online Shop is noteworthy for providing various useful daily\x01",
            "items, as well as offering many sort of tickets and passes.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #72
        (
            "\x07\x05#1SFurthermore, in the case that the Halo Rail main service is\x01",
            "inoperative for some reason, users may also engage the\x01",
            "station in Emergency Operations Mode, as well as open\x01",
            "emergency substratum passages at all terminals.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33F4")

    label("loc_31DE")


    AnonymousTalk(    #73
        (
            "\x07\x05#1SEmergency Operations Mode is, as the name implies, the\x01",
            "emergency last-ditch operation mode for the Halo Rail\x01",
            "service. Should an emergency arise in which power from the\x01",
            "Axis Pillar is cut to the Halo Rail, this mode switches the\x01",
            "rail to local backup, allowing for semi-normal operation on\x01",
            "a temporary basis.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #74
        (
            "\x07\x05#1SAs this mode is operated on a station-by-station basis,\x01",
            "should multiple stations suffer power cuts, Emergency\x01",
            "Operations Mode must be enabled at each station or they will\x01",
            "not be able to connect.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33F4")

    label("loc_33E7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_33F4")

    label("loc_33F4")

    Jump("loc_2D26")

    label("loc_33F7")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3414")

    label("loc_3407")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3414")

    label("loc_3414")

    Jump("loc_2C99")

    label("loc_3417")

    OP_5F(0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3446")

    label("loc_3427")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3446")

    label("loc_3446")

    Jump("loc_2C49")

    label("loc_3449")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    TalkEnd(0xFF)
    Return()

    # Function_9_2B53 end

    def Function_10_3472(): pass

    label("Function_10_3472")

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
        (0, "loc_34EB"),
        (1, "loc_34F1"),
        (SWITCH_DEFAULT, "loc_34F7"),
    )


    label("loc_34EB")

    OP_A2(0x1200)
    Jump("loc_34F7")

    label("loc_34F1")

    OP_A2(0x1201)
    Jump("loc_34F7")

    label("loc_34F7")

    Return()

    # Function_10_3472 end

    def Function_11_34F8(): pass

    label("Function_11_34F8")

    FadeToDark(0, 0, -1)
    OP_6D(-545830, 30000, 755590, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_11_34F8 end

    def Function_12_358B(): pass

    label("Function_12_358B")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #75
        (
            "\x07\x05#1SCradle #35: Residential Terminal #\\C035-556800015073\x01",
            "Checking ID#100W..... #20WNo match.\x01",
            "※Unable to confirm ID of terminal owner.\x01",
            "Your viewable entries are limited.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_365F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CEB")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x0, 0x0, 0x28, 0x5A, 0x1)
    OP_CC(0x1, 0x0, "Check New Recipes")
    OP_CC(0x1, 0x0, "Read Crystal")
    OP_CC(0x1, 0x0, "Stop Use")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_36CF"),
        (1, "loc_39B8"),
        (SWITCH_DEFAULT, "loc_3CC9"),
    )


    label("loc_36CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39A8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #76
        (
            "\x07\x05 ===============Recipe＃W-6894===============\x01",
            " ==============Resurrect Jelly================ \x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x32, 0x9B, 0x9, "#2CCopy data?")
    OP_CC(0x0, 0x1, 0x28, 0xF0, 0x0)
    OP_CC(0x1, 0x1, "Yes")
    OP_CC(0x1, 0x1, "No")
    OP_CC(0x2, 0x1)
    MenuEnd(0x0)
    OP_5F(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_379F"),
        (1, "loc_3997"),
        (SWITCH_DEFAULT, "loc_3997"),
    )


    label("loc_379F")

    OP_DA()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_396F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x4B)"), scpexpr(EXPR_END)), "loc_37EA")

    AnonymousTalk(    #77
        "\x07\x05#1SData has already been copied.\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_396C")

    label("loc_37EA")

    OP_AC(0x4B)

    AnonymousTalk(    #78
        "\x07\x05#1SPrinting data#100W... #20WComplete!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_5F(0x1)
    FadeToBright(300, 0)
    Sleep(100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #79
        "\x07\x00Learned the recipe for #456i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #80
        0x101,
        "#1004FWhoa! It wrote it into the Recipe Book!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38DD")

    ChrTalk(    #81
        0x102,
        "#065FHow the heck did it even do that?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3916")

    label("loc_38DD")


    ChrTalk(    #82
        0x102,
        "#1044FI wonder what the principle behind that is...\x02",
    )

    CloseMessageWindow()

    label("loc_3916")


    ChrTalk(    #83
        0x101,
        "#1015FYou got me, but that's some crazy technology.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_396C")

    Jump("loc_3994")

    label("loc_396F")


    AnonymousTalk(    #84
        "\x07\x05#1SUnable to find print target.\x02",
    )

    CloseMessageWindow()

    label("loc_3994")

    Jump("loc_39A5")

    label("loc_3997")

    OP_DA()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39A5")

    label("loc_39A5")

    Jump("loc_36CF")

    label("loc_39A8")

    OP_5F(0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3CE8")

    label("loc_39B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x418, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C48")

    AnonymousTalk(    #85
        "\x07\x05#1SBeginning read...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #86
        "\x07\x05#1S...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #87
        "\x07\x05#1S...Specified wavelength pattern found.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #88
        "\x07\x05#1SUser is authenticated as recorded recipient of a package.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #89
        "\x07\x05#1SBeginning transfer of stored item #\\W-8834-0033.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #90
        "\x07\x05#1SDownloading data...20%...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #91
        "\x07\x05#1S...40%...60%...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #92
        "\x07\x05#1S...80%... Transfer complete!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_5F(0x0)
    Sleep(200)
    OP_5F(0x0)
    Sleep(200)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #93
        "\x07\x00Received #1047i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x417, 1)

    ChrTalk(    #94
        0x101,
        (
            "#1004FTh-This is the same ore as we already\x01",
            "have, right?\x02\x03",

            "#1015FSeems like that crystal from a bit ago\x01",
            "got sent from somewhere...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x102,
        (
            "#1035FYeah.\x02\x03",

            "#1040FI don't get how it all works, but it seems like\x01",
            "this crystal is the key.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x22D9)
    Jump("loc_3CC9")

    label("loc_3C48")


    AnonymousTalk(    #96
        "\x07\x05#1SBeginning lookup...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #97
        "\x07\x05#1S...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #98
        "\x07\x05#1S...Unable to find data.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #99
        "\x07\x05#1SPlease check your crystal and try again.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_3CC9")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3CE8")

    label("loc_3CE8")

    Jump("loc_365F")

    label("loc_3CEB")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    TalkEnd(0xFF)
    Return()

    # Function_12_358B end

    def Function_13_3D14(): pass

    label("Function_13_3D14")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #100
        (
            "\x07\x05#1SCradle #35: Residential Terminal  #\\C035-556800014096\x01",
            "Checking ID#100W..... #20WNo match.\x01",
            "※Unable to confirm ID of terminal owner.\x01",
            "Your viewable entries are limited.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3DE9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4277")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x0, 0x0, 0x28, 0x5A, 0x1)
    OP_CC(0x1, 0x0, "Bulletin Board")
    OP_CC(0x1, 0x0, "Stop Use")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3E42"),
        (SWITCH_DEFAULT, "loc_4255"),
    )


    label("loc_3E42")


    AnonymousTalk(    #101
        (
            "\x07\x05#1S[Report on Heightened City Security]\x01",
            "In recent years, there has been a notable increase in\x01",
            "crime in less populated areas of the city, such as the\x01",
            "Factoria blocks. As a result of this, heightened security\x01",
            "measures were introduced, and while some citizens may\x01",
            "have experienced some inconvenience as a result, those\x01",
            "measures were designed to have the least impact possible\x01",
            "on individual freedoms.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #102
        (
            "\x07\x05#1SHowever, despite these measures, the crime rate continues\x01",
            "to increase. The council therefore asks that citizens\x01",
            "cooperate with a number of restrictions.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #103
        (
            "\x07\x05#1SThe following will apply to all citizens:\x01",
            "-Terminal use will require personal Gospel ID checks\x01",
            "-Periodic inspections will be performed in all blocks\x01",
            "-Civilian access into the Axis Pillar is restricted\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #104
        (
            "\x07\x05#1SThis heightened security may result in some inconvenience\x01",
            "for citizens, but these measures are designed to ensure\x01",
            "the safety of all residents of our fair city. We hope you\x01",
            "understand and will offer your complete cooperation.\x01",
            "-Liber Ark Security Division\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4274")

    label("loc_4255")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4274")

    label("loc_4274")

    Jump("loc_3DE9")

    label("loc_4277")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    TalkEnd(0xFF)
    Return()

    # Function_13_3D14 end

    def Function_14_42A0(): pass

    label("Function_14_42A0")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrName("Artificial Voice")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #105
        "\x07\x05Welcome to the Cradle #35 Municipal Office!\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #106
        "\x07\x05This office is currently outside normal service hours.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #107
        (
            "\x07\x05Persons with business are asked to select direct\x01",
            "service from the automated service window in the back.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_14_42A0 end

    def Function_15_43C0(): pass

    label("Function_15_43C0")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #108
        (
            "\x07\x05#1SCradle #35: Residential Terminal  #\\C035-556800014096\x01",
            "Checking ID#100W..... #20WNo match.\x01",
            "※Unable to confirm ID of terminal owner.\x01",
            "Your viewable entries are limited.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4495")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49F0")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x0, 0x0, 0x28, 0x5A, 0x1)
    OP_CC(0x1, 0x0, "Bulletin Board")
    OP_CC(0x1, 0x0, "Stop Use")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_44EE"),
        (SWITCH_DEFAULT, "loc_49CE"),
    )


    label("loc_44EE")


    AnonymousTalk(    #109
        (
            "\x07\x05#1S※[Improvements to Distribution Service and Gospel Update]\x01",
            "Here at Liber Ark City, in order to ensure our citizens\x01",
            "lead a pleasant, fulfilled life, we have established a\x01",
            "distribution service offering music and images with a theme\x01",
            "of 'healing,' which has proven popular with the citizenry,\x01",
            "but also with persons experiencing concerns regarding mental\x01",
            "and emotional ailments.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #110
        (
            "\x07\x05#1SHowever, while this service offers a significant selection,\x01",
            "it remains somewhat uniform and one-sided. As such, we have\x01",
            "been receiving a great deal of feedback from the citizenry\x01",
            "asking for it to respond to a wide variety of personal\x01",
            "tastes. In order to accommodate these opinions, our city\x01",
            "wishes to proceed with enhancing our service's variety to\x01",
            "provide all citizens with a satisfying experience.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #111
        (
            "\x07\x05#1STo that end, we will need to offer an upgrade to all\x01",
            "citizens' personal Gospels. We ask that you inquire at\x01",
            "your local city government office and undergo upgrade\x01",
            "procedures there.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #112
        (
            "\x07\x05#1SFurthermore, as this upgrade applies to all citizens, after\x01",
            "a period of time non-upgraded Gospels will become unusable.\x01",
            "We understand this may be somewhat problematic, but we\x01",
            "sincerely ask for your cooperation.\x01",
            "-Liber Ark System Administration Division\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49ED")

    label("loc_49CE")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_49ED")

    label("loc_49ED")

    Jump("loc_4495")

    label("loc_49F0")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    TalkEnd(0xFF)
    Return()

    # Function_15_43C0 end

    def Function_16_4A19(): pass

    label("Function_16_4A19")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A3E")
    Call(0, 10)
    Call(0, 21)
    AddParty(0x45, 0xFA, 0xFF)

    label("loc_4A3E")

    OP_D2(0x270003, 0x270007, 0xA)
    OP_D2(0x270013, 0x270017, 0xB)
    OP_D2(0x2700A3, 0x2700A7, 0xC)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_4A81"),
        (3, "loc_4A8E"),
        (4, "loc_4A9B"),
        (5, "loc_4AA8"),
        (6, "loc_4AB5"),
        (7, "loc_4AC2"),
        (8, "loc_4ACF"),
        (SWITCH_DEFAULT, "loc_4ADC"),
    )


    label("loc_4A81")

    OP_D2(0x70023, 0x7002B, 0xD)
    Jump("loc_4ADC")

    label("loc_4A8E")

    OP_D2(0x70033, 0x7003B, 0xD)
    Jump("loc_4ADC")

    label("loc_4A9B")

    OP_D2(0x27039B, 0x27039F, 0xD)
    Jump("loc_4ADC")

    label("loc_4AA8")

    OP_D2(0x70053, 0x7005B, 0xD)
    Jump("loc_4ADC")

    label("loc_4AB5")

    OP_D2(0x70063, 0x7006B, 0xD)
    Jump("loc_4ADC")

    label("loc_4AC2")

    OP_D2(0x70073, 0x7007B, 0xD)
    Jump("loc_4ADC")

    label("loc_4ACF")

    OP_D2(0x270083, 0x270087, 0xD)
    Jump("loc_4ADC")

    label("loc_4ADC")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_4B01"),
        (3, "loc_4B0E"),
        (4, "loc_4B1B"),
        (5, "loc_4B28"),
        (6, "loc_4B35"),
        (7, "loc_4B42"),
        (8, "loc_4B4F"),
        (SWITCH_DEFAULT, "loc_4B5C"),
    )


    label("loc_4B01")

    OP_D2(0x70023, 0x7002B, 0xE)
    Jump("loc_4B5C")

    label("loc_4B0E")

    OP_D2(0x70033, 0x7003B, 0xE)
    Jump("loc_4B5C")

    label("loc_4B1B")

    OP_D2(0x27039B, 0x27039F, 0xE)
    Jump("loc_4B5C")

    label("loc_4B28")

    OP_D2(0x70053, 0x7005B, 0xE)
    Jump("loc_4B5C")

    label("loc_4B35")

    OP_D2(0x70063, 0x7006B, 0xE)
    Jump("loc_4B5C")

    label("loc_4B42")

    OP_D2(0x70073, 0x7007B, 0xE)
    Jump("loc_4B5C")

    label("loc_4B4F")

    OP_D2(0x270083, 0x270087, 0xE)
    Jump("loc_4B5C")

    label("loc_4B5C")

    OP_6D(59810, 0, -1090, 0)
    OP_67(0, 5780, -10000, 0)
    OP_6B(4450, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 11)
    SetChrChipByIndex(0x146, 12)
    SetChrChipByIndex(0xF8, 13)
    SetChrChipByIndex(0xF9, 14)
    SetChrSubChip(0xF9, 1)
    SetChrFlags(0x146, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0xF8, 0x4)
    SetChrFlags(0xF9, 0x4)
    SetChrPos(0x146, 59020, 200, 3010, 90)
    SetChrPos(0x101, 60220, 200, 4430, 180)
    SetChrPos(0x102, 60040, 200, 1600, 0)
    SetChrPos(0xF8, 61850, 200, 4460, 180)
    SetChrPos(0xF9, 61850, 200, 1520, 0)

    def lambda_4C2B():
        OP_6D(59860, 0, 4019, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4C2B)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    Fade(500)
    OP_6D(59860, 0, 4019, 0)
    OP_67(0, 5780, -10000, 0)
    OP_6B(3510, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #113
        0x146,
        (
            "#413F#6PSorry I lost it... Guess you guys\x01",
            "didn't expect that, huh?\x02\x03",

            "#210FI...think I'm a little calmer now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        "#1019FEyes on you, Capua. Eyes. On.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x102,
        (
            "#1035F#6PAhem! So, Josette...\x02\x03",

            "#1042FCan you tell us what\x01",
            "exactly happened?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x146, 2)
    Sleep(300)

    ChrTalk(    #116
        0x146,
        (
            "#215F#7PI think so... Yeah.\x02\x03",

            "#212FSo, we managed to crash about as gracefully\x01",
            "as we could, right? And, hey, our orbments work\x01",
            "NOW, so we got to work fixing the Bobcat.\x02\x03",

            "The engine wasn't really damaged,\x01",
            "but the rest of the ship was a mess.\x02\x03",

            "We were nosing around looking\x01",
            "for material to use for repairs.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F09")

    ChrTalk(    #117
        0x106,
        "#555FGot'cha. Basically the same mess we're in.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5045")

    label("loc_4F09")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F53")

    ChrTalk(    #118
        0x108,
        "#070FThe same situation we find ourselves in, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5045")

    label("loc_4F53")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F93")

    ChrTalk(    #119
        0x103,
        "#020FI see. More or less exactly like us.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5045")

    label("loc_4F93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FCB")

    ChrTalk(    #120
        0x109,
        "#1063FSame mess we're in, really.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5045")

    label("loc_4FCB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5009")

    ChrTalk(    #121
        0x104,
        "#030FHmm. So we share in the same fate.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5045")

    label("loc_5009")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5045")

    ChrTalk(    #122
        0x105,
        "#1162FYou face the same situation we do.\x02",
    )

    CloseMessageWindow()

    label("loc_5045")


    ChrTalk(    #123
        0x146,
        (
            "#215F#7PIt was...um, three days ago now.\x02\x03",

            "We'd gotten the materials we needed and\x01",
            "were just about to start the real repair work\x01",
            "when this...octopus-like machine appeared.\x02\x03",

            "#413FAfter I shot it, a red airship showed up.\x02\x03",

            "Jaegers came flooding out of\x01",
            "it as soon as it landed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x102,
        (
            "#1043F#6PAh, of course.\x01",
            "You shot down a Vogel.\x02\x03",

            "#1035FThey use those for scouting and patrols.\x01",
            "It alerted the enemy to your location the\x01",
            "instant it was destroyed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x146,
        (
            "#216F#7PI knew it...\x02\x03",

            "#215FWhat... What do I do?\x02\x03",

            "It's all my fault Kyle and Don were taken!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x102,
        "#1043F#6PJosette...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        (
            "#1022FRrrrrgh, for the--knock it off with the\x01",
            "mopey face!\x02\x03",

            "#1005FIf they got caught,\x01",
            "let's go rescue them!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x146, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x146, 0)

    ChrTalk(    #128
        0x146,
        "#213F#6PWh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        (
            "#1006FEven if they are criminals themselves,\x01",
            "if they're being held illegally, then they\x01",
            "deserve bracer protection.\x02\x03",

            "Besides, we have some biscuits\x01",
            "to grind with the society anyway!\x02\x03",

            "We'll save your brothers while we're at it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x102,
        "#1040F#6PEstelle...\x02",
    )

    CloseMessageWindow()
    OP_62(0x146, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #131
        0x146,
        (
            "#212F#6PH-Hold on a sec!\x02\x03",

            "#214FWhat makes you think we want to\x01",
            "be saved by the likes of bracers?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#1007FHrmmm. The 'likes of bracers,' huh?\x02\x03",

            "#1028FSo you can save them all by yourself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x146,
        "#216F#6PMrgh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        (
            "#1006FBesides, you helped us when we\x01",
            "were escaping the Glorious.\x02\x03",

            "It's way past time we returned the favor!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x146,
        "#214F#6PMrrrrrrrrrrrrrrrrgh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x102,
        (
            "#1035F#6PJosette, Estelle's right.\x02\x03",

            "#1040FIf you run in on your own, you'll just\x01",
            "be caught, and you won't help\x01",
            "anyone just staying here.\x02\x03",

            "You know that, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x146,
        "#215F#6PMmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x102,
        (
            "#1040F#6PWhy don't you head to the Arseille\x01",
            "for the moment?\x02\x03",

            "#1035FI suspect Kyle and the others are\x01",
            "being kept on the Glorious.\x02\x03",

            "There's a good chance it's docked to the\x01",
            "island somewhere. If we continue to\x01",
            "investigate, I suspect we'll find it.\x02\x03",

            "#1040FWe'll tell you when we locate it.\x01",
            "I promise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x146,
        (
            "#215F#6P...\x02\x03",

            "#413FAll right. If you say so, Joshua.\x02\x03",

            "#214FI'm not gonna just sit around and\x01",
            "twiddle my thumbs, though!\x02\x03",

            "I'm gonna help too! You want me\x01",
            "to tag along, you just say so!\x01",
            "I'll even help fix your ship!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x101,
        (
            "#1016FYeah, yeah, okay. You can TRY to impress\x01",
            "all you want, but it's still too late, Miss Tomboy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x146,
        (
            "#210F#6PPssh! At least I AM impressive.\x02\x03",

            "In more ways than one compared to YOU!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        "#1019FWHAT was that?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x102,
        (
            "#1052F#6PCome on now, really...\x02\x03",

            "#1048FI don't know what it is with you two,\x01",
            "but can't you TRY to get along?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x146, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)
    OP_63(0x146)
    Sleep(500)
    SetChrSubChip(0x101, 0)

    ChrTalk(    #144
        0x101,
        "#1007F...Uh. Joshua.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x146, 2)

    ChrTalk(    #145
        0x146,
        (
            "#212F#7P...Did he just say that?\x01",
            "He just said that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x102,
        "#1044F#6PHm?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5AAF")

    ChrTalk(    #147
        0x109,
        (
            "#1068F(Oooooh, Sweet Goddess Above.\x01",
            "Nice knowin' ya, Joshua.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BCF")

    label("loc_5AAF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5AF5")

    ChrTalk(    #148
        0x104,
        (
            "#035F(You've stepped on a landmine,\x01",
            "my friend.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BCF")

    label("loc_5AF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B35")

    ChrTalk(    #149
        0x106,
        "#551F(Well, that's stepping right on it.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_5BCF")

    label("loc_5B35")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B68")

    ChrTalk(    #150
        0x108,
        "#075F(Well, he's in it now.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_5BCF")

    label("loc_5B68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BA3")

    ChrTalk(    #151
        0x103,
        "#025F(*sigh* Oh, Joshua. You idiot.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_5BCF")

    label("loc_5BA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BCF")

    ChrTalk(    #152
        0x107,
        "#065F(Oh, no, Joshua...)\x02",
    )

    CloseMessageWindow()

    label("loc_5BCF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BFE")

    ChrTalk(    #153
        0x105,
        "#1167F(You utter dunce.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D4D")

    label("loc_5BFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C2D")

    ChrTalk(    #154
        0x107,
        "#065F(Oh, no, Joshua...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D4D")

    label("loc_5C2D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C75")

    ChrTalk(    #155
        0x103,
        (
            "#025F(Oh, my student.\x01",
            "You have so much to learn.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D4D")

    label("loc_5C75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CAE")

    ChrTalk(    #156
        0x108,
        "#071F(Ahhh, the follies of youth!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D4D")

    label("loc_5CAE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CF3")

    ChrTalk(    #157
        0x106,
        "#555F(That kid seriously doesn't know fear...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D4D")

    label("loc_5CF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D4D")

    ChrTalk(    #158
        0x104,
        (
            "#031F(Hahaha! Ah, Joshua! Truly, you\x01",
            "do not know the meaning of fear!)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D4D")


    ChrTalk(    #159
        0x101,
        (
            "#1019FHey, Capua.\x02\x03",

            "Truce for the moment, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x146,
        (
            "#413F#6PAgreed.\x02\x03",

            "We have bigger fish to fry\x01",
            "than each other right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x102,
        (
            "#1048F#6PEr. Wait.\x02\x03",

            "I'm glad you two are calling a 'truce'...\x01",
            "but what 'bigger fish' are you talking about?\x01",
            "Did I...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x101,
        "#1001FOh, no, it's nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x146,
        (
            "#211F#7PNow why would you think a thing\x01",
            "like that, hmmmmm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x102,
        (
            "#1052F#6PO...kay. (Why do their smiles\x01",
            "fill me with such terror?)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F0C")
    OP_A2(0x22A4)

    label("loc_5F0C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F1D")
    OP_A2(0x229D)

    label("loc_5F1D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F2B")

    label("loc_5F2B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F3C")
    OP_A2(0x22A7)

    label("loc_5F3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F4D")
    OP_A2(0x22A0)

    label("loc_5F4D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F5E")
    OP_A2(0x22A2)

    label("loc_5F5E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F6C")

    label("loc_5F6C")

    OP_31(0xA, 0x0, 0x48)
    OP_31(0xA, 0xFE, 0x0)
    OP_41(0xA, 0x6A, 0xFF)
    OP_41(0xA, 0x105, 0xFF)
    OP_41(0xA, 0x126, 0xFF)
    OP_41(0xA, 0x132, 0xFF)
    OP_37(0xA, 0x7F, 0x2)
    OP_41(0xA, 0x29A, 0x0)
    OP_41(0xA, 0x2CB, 0x4)
    OP_41(0xA, 0x298, 0x6)
    OP_35(0xA, 0x0)
    OP_6D(-25340, 0, 52840, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrName("")

    AnonymousTalk(    #165
        (
            "\x07\x05Please form your party. You may choose two other members\x01",
            "aside from the mandatory members.\x01",
            "(Removed members will return to the Arseille.)\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    FadeToBright(0, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60BA")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0xA, 0xFFFF)
    Jump("loc_6463")

    label("loc_60BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60E9")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x4, 0xA, 0xFFFF)
    Jump("loc_6463")

    label("loc_60E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6118")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x3, 0xA, 0xFFFF)
    Jump("loc_6463")

    label("loc_6118")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6147")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x6, 0xA, 0xFFFF)
    Jump("loc_6463")

    label("loc_6147")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6176")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x7, 0xA, 0xFFFF)
    Jump("loc_6463")

    label("loc_6176")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_61A5")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x8, 0xA, 0xFFFF)
    Jump("loc_6463")

    label("loc_61A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_61D4")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x2, 0x4, 0xA, 0xFFFF)
    Jump("loc_6463")

    label("loc_61D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6203")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x2, 0x3, 0xA, 0xFFFF)
    Jump("loc_6463")

    label("loc_6203")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6232")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x2, 0x6, 0xA, 0xFFFF)
    Jump("loc_6463")

    label("loc_6232")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6261")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x2, 0x7, 0xA, 0xFFFF)
    Jump("loc_6463")

    label("loc_6261")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6290")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x2, 0x8, 0xA, 0xFFFF)
    Jump("loc_6463")

    label("loc_6290")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62BF")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x4, 0x3, 0xA, 0xFFFF)
    Jump("loc_6463")

    label("loc_62BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62EE")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x4, 0x6, 0xA, 0xFFFF)
    Jump("loc_6463")

    label("loc_62EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_631D")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x4, 0x7, 0xA, 0xFFFF)
    Jump("loc_6463")

    label("loc_631D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_634C")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x4, 0x8, 0xA, 0xFFFF)
    Jump("loc_6463")

    label("loc_634C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_637B")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x3, 0x6, 0xA, 0xFFFF)
    Jump("loc_6463")

    label("loc_637B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_63AA")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x3, 0x7, 0xA, 0xFFFF)
    Jump("loc_6463")

    label("loc_63AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_63D9")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x3, 0x8, 0xA, 0xFFFF)
    Jump("loc_6463")

    label("loc_63D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6408")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x6, 0x7, 0xA, 0xFFFF)
    Jump("loc_6463")

    label("loc_6408")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6437")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x6, 0x8, 0xA, 0xFFFF)
    Jump("loc_6463")

    label("loc_6437")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6463")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x7, 0x8, 0xA, 0xFFFF)

    label("loc_6463")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/C5801   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_4A19 end

    def Function_17_6489(): pass

    label("Function_17_6489")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_64A0")
    Call(0, 20)
    Call(0, 22)

    label("loc_64A0")

    OP_D2(0x270003, 0x270007, 0xA)
    OP_D2(0x270013, 0x270017, 0xB)
    OP_D2(0x2700A3, 0x2700A7, 0xC)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_64E3"),
        (3, "loc_64F0"),
        (4, "loc_64FD"),
        (5, "loc_650A"),
        (6, "loc_6517"),
        (7, "loc_6524"),
        (8, "loc_6531"),
        (SWITCH_DEFAULT, "loc_653E"),
    )


    label("loc_64E3")

    OP_D2(0x70023, 0x7002B, 0xD)
    Jump("loc_653E")

    label("loc_64F0")

    OP_D2(0x70033, 0x7003B, 0xD)
    Jump("loc_653E")

    label("loc_64FD")

    OP_D2(0x27039B, 0x27039F, 0xD)
    Jump("loc_653E")

    label("loc_650A")

    OP_D2(0x70053, 0x7005B, 0xD)
    Jump("loc_653E")

    label("loc_6517")

    OP_D2(0x70063, 0x7006B, 0xD)
    Jump("loc_653E")

    label("loc_6524")

    OP_D2(0x70073, 0x7007B, 0xD)
    Jump("loc_653E")

    label("loc_6531")

    OP_D2(0x270083, 0x270087, 0xD)
    Jump("loc_653E")

    label("loc_653E")

    OP_D2(0x270407, 0x27040C, 0xE)
    OP_D2(0x270408, 0x27040D, 0xF)
    OP_6D(59860, 0, 4019, 0)
    OP_67(0, 5780, -10000, 0)
    OP_6B(3510, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 11)
    SetChrChipByIndex(0x10B, 12)
    SetChrChipByIndex(0xF9, 13)
    SetChrChipByIndex(0x9, 14)
    SetChrChipByIndex(0xA, 15)
    SetChrFlags(0x10B, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0xF9, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrPos(0x10B, 59020, 200, 3010, 90)
    SetChrPos(0x9, 60220, 200, 4430, 180)
    SetChrPos(0xA, 61850, 200, 4460, 180)
    SetChrPos(0x102, 60040, 200, 1600, 0)
    SetChrPos(0x101, 61850, 200, 1520, 0)
    SetChrPos(0xF9, 62840, 200, 3040, 270)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #166
        0x9,
        (
            "#198F#7PRight, then. We're going to get\x01",
            "back to repairing the Bobcat.\x02\x03",

            "#197FWe should have all the materials\x01",
            "we need, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xA,
        (
            "#203F#4PThe real issue is that 'Orbal Shutdown\x01",
            "Phenomenon' thing.\x02\x03",

            "#206FIf we just take off, we'll drop like a stone\x01",
            "again the instant we leave the city.\x01",
            "Straight into the lake, this time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x101,
        (
            "#1015F#5PHmmm... At least without another big\x01",
            "Zero Field thingy you will, yeah.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x102,
        (
            "#1044F#5PShall we ask Professor Russell aboard\x01",
            "the Arseille to help you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xA,
        (
            "#200F#4PWe can use our radio while in the city,\x01",
            "at least, so we'll contact them ourselves.\x02\x03",

            "Meanwhile, I'm guessing you're all going\x01",
            "to continue looking for this\x01",
            "'Aureole' of yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x102,
        "#1040F#5PThat was the plan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x101,
        (
            "#1006F#5PThat was our whole reason for\x01",
            "coming here in the first place.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x10B, 2)
    Sleep(300)

    ChrTalk(    #173
        0x10B,
        (
            "#213F#6PNow that you mention it, you did\x01",
            "talk about something like that.\x02\x03",

            "So you guys weren't looking for treasure,\x01",
            "too?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 1)
    Sleep(300)

    ChrTalk(    #174
        0x101,
        (
            "#1019F#5PCapua, please don't equate yourself\x01",
            "with me. Ever.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x9)
    OP_63(0xA)
    Sleep(500)

    ChrTalk(    #175
        0xA,
        (
            "#200F#4PIn that case... Josette.\x02\x03",

            "Why don't you keep working with\x01",
            "Joshua's team?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Sleep(100)
    SetChrSubChip(0x10B, 0)
    Sleep(100)
    SetChrSubChip(0x101, 0)
    Sleep(300)

    ChrTalk(    #176
        0x10B,
        "#213F#6PHuh?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x9,
        (
            "#490F#7PThe lads and us two will be more than\x01",
            "enough to get the Bobcat repaired.\x02\x03",

            "To be honest, I wanted you out there\x01",
            "getting us information either way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x10B,
        "#210F#6PAh, okay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x102,
        (
            "#1035F#5PAnd with everything going on, having\x01",
            "someone who can coordinate between\x01",
            "the Arseille and the Bobcat would help.\x02\x03",

            "#1040FIt's a good plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x101,
        (
            "#1006F#5PYeah, I agree.\x02\x03",

            "Besides, we need all the help we\x01",
            "can get against the society.\x02\x03",

            "Josette's a great support. She'd be\x01",
            "a big help in the coming battles.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x10B, 2)
    Sleep(300)

    ChrTalk(    #181
        0x10B,
        "#213F#6P...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 1)
    Sleep(300)

    ChrTalk(    #182
        0x101,
        "#1004F#2PSomething wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x10B,
        (
            "#216F#6PNo, uh, it's just...\x02\x03",

            "#215F(Uh, Joshua. Is she serious?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x102,
        (
            "#1049F#5P(Haha... As serious as you'll\x01",
            "ever see her.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x10B,
        "#413F#6P(And there's the headache...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x101,
        "#1009F#2PHey, wait, Capua. What's with that face?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x10B,
        (
            "#210F#6POh, nothing.\x01",
            "Just total resignation that I'm at\x01",
            "the command of an airhead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x101,
        (
            "#1019F#2PHow about I order you off\x01",
            "the edge of the island, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x9,
        "#191F#7PGyahaha! That settles that, I suppose!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xA,
        (
            "#200F#4PWe'll get started here, then.\x02\x03",

            "Josette. Careful out there, all right?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x10B, 0)
    Sleep(100)
    SetChrSubChip(0x101, 0)
    Sleep(300)

    ChrTalk(    #191
        0x10B,
        (
            "#210F#6PYeah, I will be.\x01",
            "You guys be careful too, okay?\x02\x03",

            "The society might attack you guys again.\x01",
            "Call for help if they do, got it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x9,
        "#191F#7PHaha! No worries!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xA,
        "#200F#4PWe'll keep an eye out.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)

    def lambda_7048():
        OP_6D(59950, 0, 5310, 1000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7048)
    SetChrChipByIndex(0x9, 8)
    SetChrChipByIndex(0xA, 9)
    ClearChrFlags(0x9, 0x4)
    ClearChrFlags(0xA, 0x4)
    SetChrPos(0x9, 59170, 0, 4380, 270)
    SetChrPos(0xA, 62820, 0, 4390, 90)
    OP_0D()
    Sleep(500)

    def lambda_709C():
        OP_6D(59480, 0, -310, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_709C)
    OP_43(0x9, 0x1, 0x0, 0x12)
    Sleep(100)
    OP_43(0xA, 0x1, 0x0, 0x13)
    SetChrSubChip(0x10B, 1)
    Sleep(50)
    SetChrSubChip(0xF9, 2)
    Sleep(500)
    SetChrSubChip(0x102, 1)
    Sleep(50)
    SetChrSubChip(0x101, 2)
    Sleep(1000)
    SetChrSubChip(0x10B, 0)
    Sleep(50)
    SetChrSubChip(0xF9, 0)
    Sleep(1000)
    SetChrSubChip(0x10B, 2)
    Sleep(50)
    SetChrSubChip(0xF9, 1)
    OP_A2(0x222C)
    OP_28(0x9E, 0x1, 0x100)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0xA, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #194
        "#5CJosette learned the '#2CBobcat#5C' S-Craft!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_36(0xA, 0x112)
    OP_BB(0xA, 0x6, 0x112)
    OP_22(0x21E, 0x0, 0x64)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x10B, 0x4)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0xF9, 0x4)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x10B, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x10B, 0)
    SetChrSubChip(0xF9, 0)
    OP_6D(58080, 0, 600, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 58080, 0, 600, 180)
    SetChrPos(0x1, 58080, 0, 600, 180)
    SetChrPos(0x2, 58080, 0, 600, 180)
    SetChrPos(0x3, 58080, 0, 600, 180)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_17_6489 end

    def Function_18_725F(): pass

    label("Function_18_725F")

    OP_8E(0xFE, 0xE060, 0x0, 0xBB8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xEAB0, 0x0, 0xFFFFE16A, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x4)

    def lambda_7292():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7292)
    OP_8E(0xFE, 0xEAE2, 0x0, 0xFFFFDCCE, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_18_725F end

    def Function_19_72B8(): pass

    label("Function_19_72B8")

    OP_8E(0xFE, 0xFD01, 0x0, 0xD5C, 0xBB8, 0x0)
    OP_8E(0xFE, 0xF1EA, 0x0, 0xFFFFE142, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x4)

    def lambda_72EB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_72EB)
    OP_8E(0xFE, 0xF1C2, 0x0, 0xFFFFDC4C, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_19_72B8 end

    def Function_20_7311(): pass

    label("Function_20_7311")

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
        (0, "loc_738A"),
        (1, "loc_7390"),
        (SWITCH_DEFAULT, "loc_7396"),
    )


    label("loc_738A")

    OP_A2(0x1200)
    Jump("loc_7396")

    label("loc_7390")

    OP_A2(0x1201)
    Jump("loc_7396")

    label("loc_7396")

    Return()

    # Function_20_7311 end

    def Function_21_7397(): pass

    label("Function_21_7397")

    FadeToDark(0, 0, -1)
    OP_6D(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_21_7397 end

    def Function_22_7428(): pass

    label("Function_22_7428")

    FadeToDark(0, 0, -1)
    OP_6D(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
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

    # Function_22_7428 end

    SaveToFile()

Try(main)
