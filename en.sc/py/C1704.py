from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'C1704   ._SN',
        MapName             = 'Bose',
        Location            = 'C1704.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60060",
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
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
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
        'ED6_DT29/CH12800 ._CH',             # 00
        'ED6_DT29/CH12801 ._CH',             # 01
        'ED6_DT29/CH12810 ._CH',             # 02
        'ED6_DT29/CH12811 ._CH',             # 03
        'ED6_DT29/CH12820 ._CH',             # 04
        'ED6_DT29/CH12821 ._CH',             # 05
        'ED6_DT29/CH12830 ._CH',             # 06
        'ED6_DT29/CH12831 ._CH',             # 07
        'ED6_DT29/CH12840 ._CH',             # 08
        'ED6_DT29/CH12841 ._CH',             # 09
        'ED6_DT29/CH12850 ._CH',             # 0A
        'ED6_DT29/CH12851 ._CH',             # 0B
        'ED6_DT29/CH12860 ._CH',             # 0C
        'ED6_DT29/CH12861 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT29/CH12800P._CP',             # 00
        'ED6_DT29/CH12801P._CP',             # 01
        'ED6_DT29/CH12810P._CP',             # 02
        'ED6_DT29/CH12811P._CP',             # 03
        'ED6_DT29/CH12820P._CP',             # 04
        'ED6_DT29/CH12821P._CP',             # 05
        'ED6_DT29/CH12830P._CP',             # 06
        'ED6_DT29/CH12831P._CP',             # 07
        'ED6_DT29/CH12840P._CP',             # 08
        'ED6_DT29/CH12841P._CP',             # 09
        'ED6_DT29/CH12850P._CP',             # 0A
        'ED6_DT29/CH12851P._CP',             # 0B
        'ED6_DT29/CH12860P._CP',             # 0C
        'ED6_DT29/CH12861P._CP',             # 0D
    )

    DeclMonster(
        X                   = -6050,
        Z                   = 400,
        Y                   = 21750,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F4,
        Unknown_18          = 7824,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 5470,
        Z                   = 400,
        Y                   = 22210,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F5,
        Unknown_18          = 7825,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -340,
        Z                   = 400,
        Y                   = -13040,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F8,
        Unknown_18          = 7826,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -59670,
        Z                   = 8400,
        Y                   = 86010,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F4,
        Unknown_18          = 7827,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -79990,
        Z                   = 4800,
        Y                   = 31890,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F5,
        Unknown_18          = 7828,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -68390,
        Z                   = 4800,
        Y                   = 31970,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F7,
        Unknown_18          = 7829,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 79410,
        Z                   = 4800,
        Y                   = 31630,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F4,
        Unknown_18          = 7830,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 68430,
        Z                   = 4800,
        Y                   = 32280,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F5,
        Unknown_18          = 7831,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 58010,
        Z                   = 8400,
        Y                   = 90210,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F6,
        Unknown_18          = 7832,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 10,
        TriggerZ            = 0,
        TriggerY            = 22700,
        TriggerRange        = 1000,
        ActorX              = 10,
        ActorZ              = 0,
        ActorY              = 21910,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -20,
        TriggerZ            = 0,
        TriggerY            = -7300,
        TriggerRange        = 1000,
        ActorX              = -20,
        ActorZ              = 0,
        ActorY              = -7870,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -53290,
        TriggerZ            = 8000,
        TriggerY            = 86010,
        TriggerRange        = 1000,
        ActorX              = -54000,
        ActorZ              = 8000,
        ActorY              = 86010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -74010,
        TriggerZ            = 4400,
        TriggerY            = 32710,
        TriggerRange        = 1000,
        ActorX              = -74010,
        ActorZ              = 4400,
        ActorY              = 32049,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 74030,
        TriggerZ            = 4400,
        TriggerY            = 32710,
        TriggerRange        = 1000,
        ActorX              = 74030,
        ActorZ              = 4400,
        ActorY              = 32090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53290,
        TriggerZ            = 8000,
        TriggerY            = 86000,
        TriggerRange        = 1000,
        ActorX              = 53910,
        ActorZ              = 8000,
        ActorY              = 86000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 40000,
        TriggerZ            = -7600,
        TriggerY            = 5160,
        TriggerRange        = 1000,
        ActorX              = 40000,
        ActorZ              = -7600,
        ActorY              = 5160,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -40000,
        TriggerZ            = -7600,
        TriggerY            = 4800,
        TriggerRange        = 1000,
        ActorX              = -40000,
        ActorZ              = -7600,
        ActorY              = 4800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 40000,
        TriggerZ            = 0,
        TriggerY            = 66820,
        TriggerRange        = 1000,
        ActorX              = 40000,
        ActorZ              = 0,
        ActorY              = 66820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -39900,
        TriggerZ            = 0,
        TriggerY            = 67320,
        TriggerRange        = 1000,
        ActorX              = -39900,
        ActorZ              = 0,
        ActorY              = 67320,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3860,
        TriggerZ            = 4800,
        TriggerY            = -34670,
        TriggerRange        = 1200,
        ActorX              = 3860,
        ActorZ              = 6000,
        ActorY              = -34670,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 29,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3A2",          # 00, 0
        "Function_1_3ED",          # 01, 1
        "Function_2_5B1",          # 02, 2
        "Function_3_6EC",          # 03, 3
        "Function_4_81E",          # 04, 4
        "Function_5_971",          # 05, 5
        "Function_6_A86",          # 06, 6
        "Function_7_C16",          # 07, 7
        "Function_8_D68",          # 08, 8
        "Function_9_1215",         # 09, 9
        "Function_10_17D9",        # 0A, 10
        "Function_11_1E3F",        # 0B, 11
        "Function_12_24AC",        # 0C, 12
        "Function_13_2D11",        # 0D, 13
        "Function_14_2E11",        # 0E, 14
        "Function_15_2E89",        # 0F, 15
        "Function_16_2F89",        # 10, 16
        "Function_17_3001",        # 11, 17
        "Function_18_3113",        # 12, 18
        "Function_19_3194",        # 13, 19
        "Function_20_32A6",        # 14, 20
        "Function_21_3327",        # 15, 21
        "Function_22_3427",        # 16, 22
        "Function_23_349F",        # 17, 23
        "Function_24_359F",        # 18, 24
        "Function_25_3617",        # 19, 25
        "Function_26_36F6",        # 1A, 26
        "Function_27_37D5",        # 1B, 27
        "Function_28_3823",        # 1C, 28
        "Function_29_3871",        # 1D, 29
    )


    def Function_0_3A2(): pass

    label("Function_0_3A2")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_3C2"),
        (101, "loc_3C9"),
        (102, "loc_3D0"),
        (103, "loc_3D7"),
        (104, "loc_3DE"),
        (105, "loc_3E5"),
        (SWITCH_DEFAULT, "loc_3EC"),
    )


    label("loc_3C2")

    Event(0, 13)
    Jump("loc_3EC")

    label("loc_3C9")

    Event(0, 15)
    Jump("loc_3EC")

    label("loc_3D0")

    Event(0, 17)
    Jump("loc_3EC")

    label("loc_3D7")

    Event(0, 19)
    Jump("loc_3EC")

    label("loc_3DE")

    Event(0, 21)
    Jump("loc_3EC")

    label("loc_3E5")

    Event(0, 23)
    Jump("loc_3EC")

    label("loc_3EC")

    Return()

    # Function_0_3A2 end

    def Function_1_3ED(): pass

    label("Function_1_3ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FF")
    OP_6F(0x22, 0)
    Jump("loc_406")

    label("loc_3FF")

    OP_6F(0x22, 60)

    label("loc_406")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_418")
    OP_6F(0x23, 0)
    Jump("loc_41F")

    label("loc_418")

    OP_6F(0x23, 60)

    label("loc_41F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_431")
    OP_6F(0x24, 0)
    Jump("loc_438")

    label("loc_431")

    OP_6F(0x24, 60)

    label("loc_438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44A")
    OP_6F(0x25, 0)
    Jump("loc_451")

    label("loc_44A")

    OP_6F(0x25, 60)

    label("loc_451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_463")
    OP_6F(0x26, 0)
    Jump("loc_46A")

    label("loc_463")

    OP_6F(0x26, 60)

    label("loc_46A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47C")
    OP_6F(0x27, 0)
    Jump("loc_483")

    label("loc_47C")

    OP_6F(0x27, 60)

    label("loc_483")

    LoadEffect(0x0, "map\\\\mp049_21.eff")
    LoadEffect(0x1, "map\\\\mp049_22.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D2, 0)), scpexpr(EXPR_END)), "loc_4B7")
    SetChrFlags(0x8, 0x80)

    label("loc_4B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D2, 1)), scpexpr(EXPR_END)), "loc_4C3")
    SetChrFlags(0x9, 0x80)

    label("loc_4C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D2, 2)), scpexpr(EXPR_END)), "loc_4CF")
    SetChrFlags(0xA, 0x80)

    label("loc_4CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D2, 3)), scpexpr(EXPR_END)), "loc_4DB")
    SetChrFlags(0xB, 0x80)

    label("loc_4DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D2, 4)), scpexpr(EXPR_END)), "loc_4E7")
    SetChrFlags(0xC, 0x80)

    label("loc_4E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D2, 5)), scpexpr(EXPR_END)), "loc_4F3")
    SetChrFlags(0xD, 0x80)

    label("loc_4F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D2, 6)), scpexpr(EXPR_END)), "loc_4FF")
    SetChrFlags(0xE, 0x80)

    label("loc_4FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D2, 7)), scpexpr(EXPR_END)), "loc_50B")
    SetChrFlags(0xF, 0x80)

    label("loc_50B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D3, 0)), scpexpr(EXPR_END)), "loc_517")
    SetChrFlags(0x10, 0x80)

    label("loc_517")

    Call(0, 8)
    OP_1B(0x0, 0x0, 0xE)
    OP_1B(0x1, 0x0, 0x10)
    OP_1B(0x2, 0x0, 0x12)
    OP_1B(0x3, 0x0, 0x14)
    OP_1B(0x4, 0x0, 0x16)
    OP_1B(0x5, 0x0, 0x18)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A4")
    LoadEffect(0x2, "map\\\\mp027_00.eff")
    PlayEffect(0x2, 0x2, 0xFF, 3860, 6000, -34670, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_71(0x2A, 0x20)
    OP_6F(0x2A, 0)
    OP_70(0x2A, 0xFA)
    Jump("loc_5B0")

    label("loc_5A4")

    OP_72(0x2A, 0x20)
    OP_6F(0x2A, 250)

    label("loc_5B0")

    Return()

    # Function_1_3ED end

    def Function_2_5B1(): pass

    label("Function_2_5B1")

    OP_EA(0x2, 0x7F, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_689")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x22, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x29F, 1)"), scpexpr(EXPR_END)), "loc_622")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x9F\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1FB2)
    Jump("loc_686")

    label("loc_622")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x9F\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x9F\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x22, 60)
    OP_70(0x22, 0x0)

    label("loc_686")

    Jump("loc_6DE")

    label("loc_689")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05The chest is empty. And if it could eat you, it\x01",
            "would.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6DE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_5B1 end

    def Function_3_6EC(): pass

    label("Function_3_6EC")

    OP_EA(0x2, 0x80, 0x0, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x23, 0x1E)
    OP_73(0x23)
    OP_6F(0x23, 30)
    AddSepith(0x0, 0x12C)
    AddSepith(0x4, 0x64)
    AddSepith(0x5, 0x64)
    AddSepith(0x6, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #3
        (
            "Found\x01",
            "#2C#56IEarth Sepith x300\x01",
            "#62ITime Sepith x100\x01",
            "#60ISpace Sepith x100\x01",
            "#61IMirage Sepith x100#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1FB3)
    Jump("loc_80C")

    label("loc_7B5")


    AnonymousTalk(    #4
        (
            "\x07\x05Looking for more treasure? Just what kind of\x01",
            "budget do you think this game had?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_80C")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_6EC end

    def Function_4_81E(): pass

    label("Function_4_81E")

    OP_EA(0x2, 0x81, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x24, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_88F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "Found \x1F\xFA\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1FB4)
    Jump("loc_8F3")

    label("loc_88F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "Found \x1F\xFA\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFA\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x24, 60)
    OP_70(0x24, 0x0)

    label("loc_8F3")

    Jump("loc_963")

    label("loc_8F6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05You've already looted this chest. You briefly\x01",
            "pause to wonder if that's legal.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_963")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_81E end

    def Function_5_971(): pass

    label("Function_5_971")

    OP_EA(0x2, 0x82, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A49")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x25, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_9E2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "Found \x1F\xFD\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1FB5)
    Jump("loc_A46")

    label("loc_9E2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "Found \x1F\xFD\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFD\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x25, 60)
    OP_70(0x25, 0x0)

    label("loc_A46")

    Jump("loc_A78")

    label("loc_A49")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05TO BE CONTINUED.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A78")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_971 end

    def Function_6_A86(): pass

    label("Function_6_A86")

    OP_EA(0x2, 0x83, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B5E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x26, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1A, 1)"), scpexpr(EXPR_END)), "loc_AF7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        "Found \x1F\x1A\x00\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1FB6)
    Jump("loc_B5B")

    label("loc_AF7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "Found \x1F\x1A\x00\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x1A\x00\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x26, 60)
    OP_70(0x26, 0x0)

    label("loc_B5B")

    Jump("loc_C08")

    label("loc_B5E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "\x07\x05Despite your repeated searches, this chest\x01",
            "doesn't contain any invisible items. In fact,\x01",
            "it doesn't contain anything, visible or otherwise.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C08")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_A86 end

    def Function_7_C16(): pass

    label("Function_7_C16")

    OP_EA(0x2, 0x84, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CEE")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x27, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_C87")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #14
        "Found \x1F\xF7\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1FB7)
    Jump("loc_CEB")

    label("loc_C87")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "Found \x1F\xF7\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF7\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x27, 60)
    OP_70(0x27, 0x0)

    label("loc_CEB")

    Jump("loc_D5A")

    label("loc_CEE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "\x07\x05You've looted this chest already.\x01",
            "It's strange...it almost feels heavier now.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_D5A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_C16 end

    def Function_8_D68(): pass

    label("Function_8_D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 3)), scpexpr(EXPR_END)), "loc_DFA")
    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_72(0x4, 0x20)
    OP_72(0x5, 0x20)
    OP_72(0x6, 0x20)
    OP_72(0x7, 0x20)
    OP_72(0x0, 0x8)
    OP_72(0x1, 0x8)
    OP_72(0x2, 0x8)
    OP_72(0x3, 0x8)
    OP_72(0x4, 0x8)
    OP_72(0x5, 0x8)
    OP_72(0x6, 0x8)
    OP_72(0x7, 0x8)
    OP_6F(0x0, 360)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_6F(0x5, 0)
    OP_6F(0x6, 0)
    OP_6F(0x7, 0)
    Jump("loc_E82")

    label("loc_DFA")

    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_72(0x4, 0x20)
    OP_72(0x5, 0x20)
    OP_72(0x6, 0x20)
    OP_72(0x7, 0x20)
    OP_72(0x0, 0x8)
    OP_72(0x1, 0x8)
    OP_72(0x2, 0x8)
    OP_72(0x3, 0x8)
    OP_72(0x4, 0x8)
    OP_72(0x5, 0x8)
    OP_72(0x6, 0x8)
    OP_72(0x7, 0x8)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_6F(0x5, 0)
    OP_6F(0x6, 0)
    OP_6F(0x7, 0)

    label("loc_E82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C6, 2)), scpexpr(EXPR_END)), "loc_F14")
    OP_72(0x8, 0x20)
    OP_72(0x9, 0x20)
    OP_72(0xA, 0x20)
    OP_72(0xB, 0x20)
    OP_72(0xC, 0x20)
    OP_72(0xD, 0x20)
    OP_72(0xE, 0x20)
    OP_72(0xF, 0x20)
    OP_72(0x8, 0x8)
    OP_72(0x9, 0x8)
    OP_72(0xA, 0x8)
    OP_72(0xB, 0x8)
    OP_72(0xC, 0x8)
    OP_72(0xD, 0x8)
    OP_72(0xE, 0x8)
    OP_72(0xF, 0x8)
    OP_6F(0x8, 360)
    OP_6F(0x9, 0)
    OP_6F(0xA, 0)
    OP_6F(0xB, 0)
    OP_6F(0xC, 0)
    OP_6F(0xD, 0)
    OP_6F(0xE, 0)
    OP_6F(0xF, 0)
    Jump("loc_F9C")

    label("loc_F14")

    OP_72(0x8, 0x20)
    OP_72(0x9, 0x20)
    OP_72(0xA, 0x20)
    OP_72(0xB, 0x20)
    OP_72(0xC, 0x20)
    OP_72(0xD, 0x20)
    OP_72(0xE, 0x20)
    OP_72(0xF, 0x20)
    OP_72(0x8, 0x8)
    OP_72(0x9, 0x8)
    OP_72(0xA, 0x8)
    OP_72(0xB, 0x8)
    OP_72(0xC, 0x8)
    OP_72(0xD, 0x8)
    OP_72(0xE, 0x8)
    OP_72(0xF, 0x8)
    OP_6F(0x8, 0)
    OP_6F(0x9, 0)
    OP_6F(0xA, 0)
    OP_6F(0xB, 0)
    OP_6F(0xC, 0)
    OP_6F(0xD, 0)
    OP_6F(0xE, 0)
    OP_6F(0xF, 0)

    label("loc_F9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C6, 3)), scpexpr(EXPR_END)), "loc_103F")
    OP_72(0x19, 0x20)
    OP_72(0x1A, 0x20)
    OP_72(0x1B, 0x20)
    OP_72(0x1C, 0x20)
    OP_72(0x1D, 0x20)
    OP_72(0x1E, 0x20)
    OP_72(0x1F, 0x20)
    OP_72(0x20, 0x20)
    OP_72(0x21, 0x20)
    OP_72(0x19, 0x8)
    OP_72(0x1A, 0x8)
    OP_72(0x1B, 0x8)
    OP_72(0x1C, 0x8)
    OP_72(0x1D, 0x8)
    OP_72(0x1E, 0x8)
    OP_72(0x1F, 0x8)
    OP_72(0x20, 0x8)
    OP_72(0x21, 0x8)
    OP_6F(0x19, 360)
    OP_6F(0x1A, 0)
    OP_6F(0x1B, 0)
    OP_6F(0x1C, 0)
    OP_6F(0x1D, 0)
    OP_6F(0x1E, 0)
    OP_6F(0x1F, 0)
    OP_6F(0x20, 0)
    OP_6F(0x21, 0)
    Jump("loc_10D8")

    label("loc_103F")

    OP_72(0x19, 0x20)
    OP_72(0x1A, 0x20)
    OP_72(0x1B, 0x20)
    OP_72(0x1C, 0x20)
    OP_72(0x1D, 0x20)
    OP_72(0x1E, 0x20)
    OP_72(0x1F, 0x20)
    OP_72(0x20, 0x20)
    OP_72(0x21, 0x20)
    OP_72(0x19, 0x8)
    OP_72(0x1A, 0x8)
    OP_72(0x1B, 0x8)
    OP_72(0x1C, 0x8)
    OP_72(0x1D, 0x8)
    OP_72(0x1E, 0x8)
    OP_72(0x1F, 0x8)
    OP_72(0x20, 0x8)
    OP_72(0x21, 0x8)
    OP_6F(0x19, 0)
    OP_6F(0x1A, 0)
    OP_6F(0x1B, 0)
    OP_6F(0x1C, 0)
    OP_6F(0x1D, 0)
    OP_6F(0x1E, 0)
    OP_6F(0x1F, 0)
    OP_6F(0x20, 0)
    OP_6F(0x21, 0)

    label("loc_10D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C6, 4)), scpexpr(EXPR_END)), "loc_117B")
    OP_72(0x10, 0x20)
    OP_72(0x11, 0x20)
    OP_72(0x12, 0x20)
    OP_72(0x13, 0x20)
    OP_72(0x14, 0x20)
    OP_72(0x15, 0x20)
    OP_72(0x16, 0x20)
    OP_72(0x17, 0x20)
    OP_72(0x18, 0x20)
    OP_72(0x10, 0x8)
    OP_72(0x11, 0x8)
    OP_72(0x12, 0x8)
    OP_72(0x13, 0x8)
    OP_72(0x14, 0x8)
    OP_72(0x15, 0x8)
    OP_72(0x16, 0x8)
    OP_72(0x17, 0x8)
    OP_72(0x18, 0x8)
    OP_6F(0x10, 360)
    OP_6F(0x11, 0)
    OP_6F(0x12, 0)
    OP_6F(0x13, 0)
    OP_6F(0x14, 0)
    OP_6F(0x15, 0)
    OP_6F(0x16, 0)
    OP_6F(0x17, 0)
    OP_6F(0x18, 0)
    Jump("loc_1214")

    label("loc_117B")

    OP_72(0x10, 0x20)
    OP_72(0x11, 0x20)
    OP_72(0x12, 0x20)
    OP_72(0x13, 0x20)
    OP_72(0x14, 0x20)
    OP_72(0x15, 0x20)
    OP_72(0x16, 0x20)
    OP_72(0x17, 0x20)
    OP_72(0x18, 0x20)
    OP_72(0x10, 0x8)
    OP_72(0x11, 0x8)
    OP_72(0x12, 0x8)
    OP_72(0x13, 0x8)
    OP_72(0x14, 0x8)
    OP_72(0x15, 0x8)
    OP_72(0x16, 0x8)
    OP_72(0x17, 0x8)
    OP_72(0x18, 0x8)
    OP_6F(0x10, 0)
    OP_6F(0x11, 0)
    OP_6F(0x12, 0)
    OP_6F(0x13, 0)
    OP_6F(0x14, 0)
    OP_6F(0x15, 0)
    OP_6F(0x16, 0)
    OP_6F(0x17, 0)
    OP_6F(0x18, 0)

    label("loc_1214")

    Return()

    # Function_8_D68 end

    def Function_9_1215(): pass

    label("Function_9_1215")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15C7")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    OP_B0(0x0, 0x78)
    OP_70(0x0, 0x168)
    Sleep(2500)
    OP_22(0x9D, 0x0, 0x64)
    OP_B0(0x4, 0x64)
    OP_B0(0x5, 0x64)
    OP_B0(0x6, 0x64)
    OP_B0(0x7, 0x64)
    OP_70(0x4, 0xF0)
    Sleep(100)
    OP_70(0x5, 0xF0)
    Sleep(100)
    OP_70(0x6, 0xF0)
    Sleep(100)
    OP_70(0x7, 0xF0)
    Sleep(100)
    OP_22(0xB9, 0x0, 0x64)
    OP_B0(0x1, 0x64)
    OP_B0(0x2, 0x64)
    OP_B0(0x3, 0x64)
    OP_70(0x1, 0x168)
    OP_70(0x2, 0x168)
    OP_70(0x3, 0x168)
    OP_73(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #17
        (
            "\x07\x05#1S[About the Device Towers 1/4]\x01",
            "■■■ First ■■r■■■r ■■■ acti■a■ed ■■■■■ssfu■■■, and\x01",
            "w■ had s■■■ee■■d in p■■■orming a ■■mpo■■■ ■■ee■e\x01",
            "upon the Aur■ole in a■■■her ■■■■■■■■■. H■■ever,\x01",
            "■■at was ■■■ the ■■nly ba■■ie■ withi■ the ■■■■ to\x01",
            "seal th■ A■■■ol■.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #18
        (
            "\x07\x05#1SThe p■■■'s ■■nal de■en■e line, the ■■■ond Ba■ri■■.\x01",
            "--The ■■■ to th■t lies ■■thin the fo■■ De■i■■\x01",
            "■o■ers.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #19
        "\x07\x00Received #1033i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x409, 1)
    OP_A2(0x1E23)
    Sleep(100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x0, 360)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_6F(0x5, 0)
    OP_6F(0x6, 0)
    OP_6F(0x7, 0)
    OP_6D(39870, -7400, 2790, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 39870, -7400, 2790, 0)
    SetChrPos(0x1, 39870, -7400, 2790, 0)
    SetChrPos(0x2, 39870, -7400, 2790, 0)
    SetChrPos(0x3, 39870, -7400, 2790, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Jump("loc_17D5")

    label("loc_15C7")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #20
        (
            "\x07\x05#1S[About the Device Towers 1/4]\x01",
            "■■■ First ■■r■■■r ■■■ acti■a■ed ■■■■■ssfu■■■, and\x01",
            "w■ had s■■■ee■■d in p■■■orming a ■■mpo■■■ ■■ee■e\x01",
            "upon the Aur■ole in a■■■her ■■■■■■■■■. H■■ever,\x01",
            "■■at was ■■■ the ■■nly ba■■ie■ withi■ the ■■■■ to\x01",
            "seal th■ A■■■ol■.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #21
        (
            "\x07\x05#1SThe p■■■'s ■■nal de■en■e line, the ■■■ond Ba■ri■■.\x01",
            "--The ■■■ to th■t lies ■■thin the fo■■ De■i■■\x01",
            "■o■ers.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_17D5")

    TalkEnd(0xFF)
    Return()

    # Function_9_1215 end

    def Function_10_17D9(): pass

    label("Function_10_17D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BE2")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    OP_B0(0x8, 0x78)
    OP_70(0x8, 0x168)
    Sleep(2500)
    OP_22(0x9D, 0x0, 0x64)
    OP_B0(0xC, 0x64)
    OP_B0(0xD, 0x64)
    OP_B0(0xE, 0x64)
    OP_B0(0xF, 0x64)
    OP_70(0xC, 0xF0)
    Sleep(100)
    OP_70(0xD, 0xF0)
    Sleep(100)
    OP_70(0xE, 0xF0)
    Sleep(100)
    OP_70(0xF, 0xF0)
    Sleep(100)
    OP_22(0xB9, 0x0, 0x64)
    OP_B0(0x9, 0x64)
    OP_B0(0xA, 0x64)
    OP_B0(0xB, 0x64)
    OP_B0(0x9, 0x64)
    OP_B0(0xA, 0x64)
    OP_B0(0xB, 0x64)
    OP_70(0x9, 0x168)
    OP_70(0xA, 0x168)
    OP_70(0xB, 0x168)
    OP_73(0x9)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #22
        (
            "\x07\x05#1S[About the Device Towers 2/4]\x01",
            "This ■■■hanis■ is ■■ilt to ■■■■■■e should ■he\x01",
            "F■■■t ■arr■■r ■■ll and tim■ once ■■■■■ tick ■n the\x01",
            "■■■ce of th■ Aure■■e. ■■■ ■■■■■■ B■rri■■'s ■ther\x01",
            "na■e is ■■e ■■a■ity ■■■■■■, and ■■ can ■ani■■■t\x01",
            "■■■■■■ ins■■e the ■■h■■ dimension.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #23
        (
            "\x07\x05#1SS■■■d the ■ur■■■e resume ■ct■■■ty, by ty■■■ th■s\x01",
            "other ■■■en■■■n do■■ wi■h ■■■chp■■s of g■■■ity,\x01",
            "the goal ■■s t■ prevent ■■■ ■■■■■■ to reality.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #24
        "\x07\x00Received #1042i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x412, 1)
    OP_A2(0x1E32)
    Sleep(100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x8, 360)
    OP_6F(0x9, 0)
    OP_6F(0xA, 0)
    OP_6F(0xB, 0)
    OP_6F(0xC, 0)
    OP_6F(0xD, 0)
    OP_6F(0xE, 0)
    OP_6F(0xF, 0)
    OP_6D(-40200, -7400, 2800, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -40200, -7400, 2800, 0)
    SetChrPos(0x1, -40200, -7400, 2800, 0)
    SetChrPos(0x2, -40200, -7400, 2800, 0)
    SetChrPos(0x3, -40200, -7400, 2800, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Jump("loc_1E3B")

    label("loc_1BE2")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #25
        (
            "\x07\x05#1S[About the Device Towers 2/4]\x01",
            "This ■■■hanis■ is ■■ilt to ■■■■■■e should ■he\x01",
            "F■■■t ■arr■■r ■■ll and tim■ once ■■■■■ tick ■n the\x01",
            "■■■ce of th■ Aure■■e. ■■■ ■■■■■■ B■rri■■'s ■ther\x01",
            "na■e is ■■e ■■a■ity ■■■■■■, and ■■ can ■ani■■■t\x01",
            "■■■■■■ ins■■e the ■■h■■ dimension.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #26
        (
            "\x07\x05#1SS■■■d the ■ur■■■e resume ■ct■■■ty, by ty■■■ th■s\x01",
            "other ■■■en■■■n do■■ wi■h ■■■chp■■s of g■■■ity,\x01",
            "the goal ■■s t■ prevent ■■■ ■■■■■■ to reality.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1E3B")

    TalkEnd(0xFF)
    Return()

    # Function_10_17D9 end

    def Function_11_1E3F(): pass

    label("Function_11_1E3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2251")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    OP_B0(0x19, 0x78)
    OP_70(0x19, 0x168)
    Sleep(2500)
    OP_22(0x9D, 0x0, 0x64)
    OP_B0(0x1D, 0x64)
    OP_B0(0x1E, 0x64)
    OP_B0(0x1F, 0x64)
    OP_B0(0x20, 0x64)
    OP_B0(0x21, 0x64)
    OP_70(0x1D, 0xF0)
    Sleep(100)
    OP_70(0x1E, 0xF0)
    Sleep(100)
    OP_70(0x1F, 0xF0)
    Sleep(100)
    OP_70(0x20, 0xF0)
    Sleep(100)
    OP_70(0x21, 0xF0)
    Sleep(100)
    OP_22(0xB9, 0x0, 0x64)
    OP_B0(0x1A, 0x64)
    OP_B0(0x1B, 0x64)
    OP_B0(0x1C, 0x64)
    OP_70(0x1A, 0x168)
    OP_70(0x1B, 0x168)
    OP_70(0x1C, 0x168)
    OP_73(0x1A)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #27
        (
            "\x07\x05#1S[About the Device Towers 3/4]\x01",
            "I ■ the ■■con■ Ba■■■■er act■■■■s, it ■■g■■ls that\x01",
            "the ■■reole is ■■■e again a■■i■e. As a ■■■■■■,\x01",
            "with its ■ospe■s, anyone ■■■l be fr■■ to ■ra■\x01",
            "out ■■■ power.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #28
        (
            "\x07\x05#1S■■■ ■■■■■■■ re■ain■■■ on L■■■r ■■■ were sealed\x01",
            "w■■h the Aur■■le. ■■■ev■r, should ■■methin■ that\x01",
            "could ■■■■■ in pl■■e ■■ ■■■ G■■■els be ■■■■ in the\x01",
            "world ■■ come, the ■ureole w■■l be f■ee to ■■eld\x01",
            "its ■■■■■ in ■■■■■■ again.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #29
        "\x07\x00Received #1043i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x413, 1)
    OP_A2(0x1E33)
    Sleep(100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x19, 360)
    OP_6F(0x1A, 0)
    OP_6F(0x1B, 0)
    OP_6F(0x1C, 0)
    OP_6F(0x1D, 0)
    OP_6F(0x1E, 0)
    OP_6F(0x1F, 0)
    OP_6F(0x20, 0)
    OP_6F(0x21, 0)
    OP_6D(39700, 200, 64819, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 39700, 200, 64819, 0)
    SetChrPos(0x1, 39700, 200, 64819, 0)
    SetChrPos(0x2, 39700, 200, 64819, 0)
    SetChrPos(0x3, 39700, 200, 64819, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Jump("loc_24A8")

    label("loc_2251")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #30
        (
            "\x07\x05#1S[About the Device Towers 3/4]\x01",
            "I ■ the ■■con■ Ba■■■■er act■■■■s, it ■■g■■ls that\x01",
            "the ■■reole is ■■■e again a■■i■e. As a ■■■■■■,\x01",
            "with its ■ospe■s, anyone ■■■l be fr■■ to ■ra■\x01",
            "out ■■■ power.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #31
        (
            "\x07\x05#1S■■■ ■■■■■■■ re■ain■■■ on L■■■r ■■■ were sealed\x01",
            "w■■h the Aur■■le. ■■■ev■r, should ■■methin■ that\x01",
            "could ■■■■■ in pl■■e ■■ ■■■ G■■■els be ■■■■ in the\x01",
            "world ■■ come, the ■ureole w■■l be f■ee to ■■eld\x01",
            "its ■■■■■ in ■■■■■■ again.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_24A8")

    TalkEnd(0xFF)
    Return()

    # Function_11_1E3F end

    def Function_12_24AC(): pass

    label("Function_12_24AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29BA")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    OP_B0(0x10, 0x78)
    OP_70(0x10, 0x168)
    Sleep(2500)
    OP_22(0x9D, 0x0, 0x64)
    OP_B0(0x14, 0x64)
    OP_B0(0x15, 0x64)
    OP_B0(0x16, 0x64)
    OP_B0(0x17, 0x64)
    OP_B0(0x18, 0x64)
    OP_70(0x14, 0xF0)
    Sleep(100)
    OP_70(0x15, 0xF0)
    Sleep(100)
    OP_70(0x16, 0xF0)
    Sleep(100)
    OP_70(0x17, 0xF0)
    Sleep(100)
    OP_70(0x18, 0xF0)
    Sleep(100)
    OP_22(0xB9, 0x0, 0x64)
    OP_B0(0x11, 0x64)
    OP_B0(0x12, 0x64)
    OP_B0(0x13, 0x64)
    OP_70(0x11, 0x168)
    OP_70(0x12, 0x168)
    OP_70(0x13, 0x168)
    OP_73(0x13)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #32
        (
            "\x07\x05#1S[About the Device Towers 4/4]\x01",
            "We ■■■■eeded in ■■■ling the ■■■eol■, but ■■■ power\x01",
            "has ■ot been d■■■roye■. ■■ will ■oot ■■■selves to\x01",
            "this la■d ■■■ ■■■■■ over ■he ■■■eole. I ■■■y t■■■\x01",
            "we ■ill be suc■■■ful in ■■■ ■■■■■ an■ ■■at t■■■e\x01",
            "records ■■■ never see■ by ■■y ■■■s.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #33
        (
            "\x07\x05#1S■■■■■■, wh■■e we are ■■■ad■■■t in our ■■■■, we\x01",
            "p■ed■■t that s■ch will ■■■ be our ■■tu■e. Wh■■ the\x01",
            "Aureole once ■ga■n ■■■■■■ to ■eal■■y, how w■ll\x01",
            "our des■■■de■■■ ch■■se to ■■■■■■? Be■■evin■ that\x01",
            "■■ wi■■ ■ot make ■■■ same ■■■■a■e again, ■■■ ■■■\x01",
            "tim■ will ■■me w■■■ we are tr■■y ■■ee of the\x01",
            "Au■■■le, I ■■■ve these reco■■s for the ■■■■■■.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #34
        "\x07\x00Received #1044i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x414, 1)
    OP_A2(0x1E34)
    Sleep(100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10, 360)
    OP_6F(0x11, 0)
    OP_6F(0x12, 0)
    OP_6F(0x13, 0)
    OP_6F(0x14, 0)
    OP_6F(0x15, 0)
    OP_6F(0x16, 0)
    OP_6F(0x17, 0)
    OP_6F(0x18, 0)
    OP_6D(-39880, 200, 64769, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -39880, 200, 64769, 0)
    SetChrPos(0x1, -39880, 200, 64769, 0)
    SetChrPos(0x2, -39880, 200, 64769, 0)
    SetChrPos(0x3, -39880, 200, 64769, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Jump("loc_2D0D")

    label("loc_29BA")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #35
        (
            "\x07\x05#1S[About the Device Towers 4/4]\x01",
            "We ■■■■eeded in ■■■ling the ■■■eol■, but ■■■ power\x01",
            "has ■ot been d■■■roye■. ■■ will ■oot ■■■selves to\x01",
            "this la■d ■■■ ■■■■■ over ■he ■■■eole. I ■■■y t■■■\x01",
            "we ■ill be suc■■■ful in ■■■ ■■■■■ an■ ■■at t■■■e\x01",
            "records ■■■ never see■ by ■■y ■■■s.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #36
        (
            "\x07\x05#1S■■■■■■, wh■■e we are ■■■ad■■■t in our ■■■■, we\x01",
            "p■ed■■t that s■ch will ■■■ be our ■■tu■e. Wh■■ the\x01",
            "Aureole once ■ga■n ■■■■■■ to ■eal■■y, how w■ll\x01",
            "our des■■■de■■■ ch■■se to ■■■■■■? Be■■evin■ that\x01",
            "■■ wi■■ ■ot make ■■■ same ■■■■a■e again, ■■■ ■■■\x01",
            "tim■ will ■■me w■■■ we are tr■■y ■■ee of the\x01",
            "Au■■■le, I ■■■ve these reco■■s for the ■■■■■■.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2D0D")

    TalkEnd(0xFF)
    Return()

    # Function_12_24AC end

    def Function_13_2D11(): pass

    label("Function_13_2D11")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 250, 52600, 0)
    SetChrPos(0x101, 500, 250, 52100, 180)
    SetChrPos(0x102, -500, 250, 52100, 180)
    SetChrPos(0xF8, 500, 250, 53100, 180)
    SetChrPos(0xF9, -500, 250, 53100, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 25)
    Call(0, 27)
    Fade(500)
    OP_6D(50, 250, 50650, 0)
    SetChrPos(0x0, 50, 250, 50650, 180)
    SetChrPos(0x1, 50, 250, 50650, 180)
    SetChrPos(0x2, 50, 250, 50650, 180)
    SetChrPos(0x3, 50, 250, 50650, 180)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_13_2D11 end

    def Function_14_2E11(): pass

    label("Function_14_2E11")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 250, 52600, 0)
    SetChrPos(0x101, -500, 250, 53100, 0)
    SetChrPos(0x102, 500, 250, 53100, 0)
    SetChrPos(0xF8, -500, 250, 52100, 0)
    SetChrPos(0xF9, 500, 250, 52100, 0)
    OP_0D()
    Call(0, 25)
    Call(0, 28)
    NewScene("ED6_DT21/C1703   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_14_2E11 end

    def Function_15_2E89(): pass

    label("Function_15_2E89")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-15500, 250, 68000, 0)
    SetChrPos(0x101, -16000, 250, 67500, 270)
    SetChrPos(0x102, -16000, 250, 68500, 270)
    SetChrPos(0xF8, -15000, 250, 67500, 270)
    SetChrPos(0xF9, -15000, 250, 68500, 270)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 25)
    Call(0, 27)
    Fade(500)
    OP_6D(-17580, 250, 67930, 0)
    SetChrPos(0x0, -17580, 250, 67930, 270)
    SetChrPos(0x1, -17580, 250, 67930, 270)
    SetChrPos(0x2, -17580, 250, 67930, 270)
    SetChrPos(0x3, -17580, 250, 67930, 270)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_15_2E89 end

    def Function_16_2F89(): pass

    label("Function_16_2F89")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-15500, 250, 68000, 0)
    SetChrPos(0x101, -15000, 250, 68500, 90)
    SetChrPos(0x102, -15000, 250, 67500, 90)
    SetChrPos(0xF8, -16000, 250, 68500, 90)
    SetChrPos(0xF9, -16000, 250, 67500, 90)
    OP_0D()
    Call(0, 25)
    Call(0, 28)
    NewScene("ED6_DT21/C1703   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_16_2F89 end

    def Function_17_3001(): pass

    label("Function_17_3001")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(15500, 250, 68000, 0)
    OP_6C(315000, 0)
    SetChrPos(0x101, 16000, 250, 68500, 90)
    SetChrPos(0x102, 16000, 250, 67500, 90)
    SetChrPos(0xF8, 15000, 250, 68500, 90)
    SetChrPos(0xF9, 15000, 250, 67500, 90)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 25)
    Call(0, 27)
    Fade(500)
    OP_6D(17480, 250, 68100, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0, 17480, 250, 68100, 90)
    SetChrPos(0x1, 17480, 250, 68100, 90)
    SetChrPos(0x2, 17480, 250, 68100, 90)
    SetChrPos(0x3, 17480, 250, 68100, 90)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_17_3001 end

    def Function_18_3113(): pass

    label("Function_18_3113")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(15500, 250, 68000, 0)
    OP_6C(315000, 0)
    SetChrPos(0x101, 15000, 250, 67500, 270)
    SetChrPos(0x102, 15000, 250, 68500, 270)
    SetChrPos(0xF8, 16000, 250, 67500, 270)
    SetChrPos(0xF9, 16000, 250, 68500, 270)
    OP_0D()
    Call(0, 25)
    Call(0, 28)
    NewScene("ED6_DT21/C1703   ._SN", 107, 0, 0)
    IdleLoop()
    Return()

    # Function_18_3113 end

    def Function_19_3194(): pass

    label("Function_19_3194")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(21500, 8200, 86000, 0)
    OP_6C(315000, 0)
    SetChrPos(0x101, 22000, 8200, 86500, 90)
    SetChrPos(0x102, 22000, 8200, 85500, 90)
    SetChrPos(0xF8, 21000, 8200, 86500, 90)
    SetChrPos(0xF9, 21000, 8200, 85500, 90)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 25)
    Call(0, 27)
    Fade(500)
    OP_6D(23620, 8200, 86140, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0, 23620, 8200, 86140, 90)
    SetChrPos(0x1, 23620, 8200, 86140, 90)
    SetChrPos(0x2, 23620, 8200, 86140, 90)
    SetChrPos(0x3, 23620, 8200, 86140, 90)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_19_3194 end

    def Function_20_32A6(): pass

    label("Function_20_32A6")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(21500, 8200, 86000, 0)
    OP_6C(315000, 0)
    SetChrPos(0x101, 21000, 8200, 85500, 270)
    SetChrPos(0x102, 21000, 8200, 86500, 270)
    SetChrPos(0xF8, 22000, 8200, 85500, 270)
    SetChrPos(0xF9, 22000, 8200, 86500, 270)
    OP_0D()
    Call(0, 25)
    Call(0, 28)
    NewScene("ED6_DT21/C1703   ._SN", 108, 0, 0)
    IdleLoop()
    Return()

    # Function_20_32A6 end

    def Function_21_3327(): pass

    label("Function_21_3327")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-21500, 8200, 86000, 0)
    SetChrPos(0x101, -22000, 8200, 85500, 270)
    SetChrPos(0x102, -22000, 8200, 86500, 270)
    SetChrPos(0xF8, -21000, 8200, 85500, 270)
    SetChrPos(0xF9, -21000, 8200, 86500, 270)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 25)
    Call(0, 27)
    Fade(500)
    OP_6D(-23480, 8200, 85910, 0)
    SetChrPos(0x0, -23480, 8200, 85910, 270)
    SetChrPos(0x1, -23480, 8200, 85910, 270)
    SetChrPos(0x2, -23480, 8200, 85910, 270)
    SetChrPos(0x3, -23480, 8200, 85910, 270)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_21_3327 end

    def Function_22_3427(): pass

    label("Function_22_3427")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-21500, 8200, 86000, 0)
    SetChrPos(0x101, -21000, 8200, 86500, 90)
    SetChrPos(0x102, -21000, 8200, 85500, 90)
    SetChrPos(0xF8, -22000, 8200, 86500, 90)
    SetChrPos(0xF9, -22000, 8200, 85500, 90)
    OP_0D()
    Call(0, 25)
    Call(0, 28)
    NewScene("ED6_DT21/C1703   ._SN", 109, 0, 0)
    IdleLoop()
    Return()

    # Function_22_3427 end

    def Function_23_349F(): pass

    label("Function_23_349F")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 5550, -27800, 0)
    SetChrPos(0x101, 500, 5550, -28300, 180)
    SetChrPos(0x102, -500, 5550, -28300, 180)
    SetChrPos(0xF8, 500, 5550, -27300, 180)
    SetChrPos(0xF9, -500, 5550, -27300, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 26)
    Call(0, 27)
    Fade(500)
    OP_6D(20, 5200, -30080, 0)
    SetChrPos(0x0, 20, 5200, -30080, 180)
    SetChrPos(0x1, 20, 5200, -30080, 180)
    SetChrPos(0x2, 20, 5200, -30080, 180)
    SetChrPos(0x3, 20, 5200, -30080, 180)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_23_349F end

    def Function_24_359F(): pass

    label("Function_24_359F")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 5550, -27800, 0)
    SetChrPos(0x101, -500, 5550, -27300, 0)
    SetChrPos(0x102, 500, 5550, -27300, 0)
    SetChrPos(0xF8, -500, 5550, -28300, 0)
    SetChrPos(0xF9, 500, 5550, -28300, 0)
    OP_0D()
    Call(0, 26)
    Call(0, 28)
    NewScene("ED6_DT21/C1705   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_24_359F end

    def Function_25_3617(): pass

    label("Function_25_3617")

    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_25_3617 end

    def Function_26_36F6(): pass

    label("Function_26_36F6")

    PlayEffect(0x1, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_26_36F6 end

    def Function_27_37D5(): pass

    label("Function_27_37D5")


    def lambda_37DB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_37DB)

    def lambda_37ED():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_37ED)

    def lambda_37FF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_37FF)

    def lambda_3811():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3811)
    Sleep(2500)
    Return()

    # Function_27_37D5 end

    def Function_28_3823(): pass

    label("Function_28_3823")


    def lambda_3829():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3829)

    def lambda_383B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_383B)

    def lambda_384D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_384D)

    def lambda_385F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_385F)
    Sleep(2000)
    Return()

    # Function_28_3823 end

    def Function_29_3871(): pass

    label("Function_29_3871")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38D7")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #37
        "\x07\x05Orbal energy appears to be shut down.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_3A79")

    label("loc_38D7")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #38
        "\x07\x05There is an orbment charging station here.\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A5E")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_72(0x2A, 0x20)
    OP_6F(0x2A, 300)
    OP_70(0x2A, 0x1F4)
    OP_73(0x2A)
    OP_6F(0x2A, 500)
    OP_70(0x2A, 0x2BC)
    OP_71(0x2A, 0x20)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x2, 0x2)
    LoadEffect(0x3, "map\\\\mp027_01.eff")
    PlayEffect(0x3, 0x3, 0xFF, 3860, 6000, -34670, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1500, 0, -1)
    Sleep(1500)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x3, 0x2)
    PlayEffect(0x2, 0x2, 0xFF, 3860, 6000, -34670, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x2A, 0)
    OP_70(0x2A, 0xFA)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_3A5E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A78")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_3A78")

    Return()

    label("loc_3A79")

    Return()

    # Function_29_3871 end

    SaveToFile()

Try(main)
