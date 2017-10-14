from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5700   ._SN',
        MapName             = 'Other',
        Location            = 'C5700.x',
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
        'Industrial Block - Factoria',          # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
        '',                                     # 19
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
        'ED6_DT29/CH12060 ._CH',             # 00
        'ED6_DT29/CH12061 ._CH',             # 01
        'ED6_DT29/CH12190 ._CH',             # 02
        'ED6_DT29/CH12191 ._CH',             # 03
        'ED6_DT29/CH12970 ._CH',             # 04
        'ED6_DT29/CH12971 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT29/CH12060P._CP',             # 00
        'ED6_DT29/CH12061P._CP',             # 01
        'ED6_DT29/CH12190P._CP',             # 02
        'ED6_DT29/CH12191P._CP',             # 03
        'ED6_DT29/CH12970P._CP',             # 04
        'ED6_DT29/CH12971P._CP',             # 05
    )

    DeclNpc(
        X                   = -1870,
        Z                   = 4000,
        Y                   = 70500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -1660,
        Z                   = 4000,
        Y                   = -82810,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x514,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -2200,
        Z                   = 4000,
        Y                   = -35950,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x515,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -2080,
        Z                   = 4000,
        Y                   = 6660,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x514,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -33090,
        Z                   = 4000,
        Y                   = -85830,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x515,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -63370,
        Z                   = 4000,
        Y                   = -95010,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x516,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -65340,
        Z                   = 4000,
        Y                   = -75570,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x516,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -23570,
        Z                   = 4000,
        Y                   = 39810,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x516,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -23470,
        Z                   = 4000,
        Y                   = -28170,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x516,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 54520,
        Z                   = 4000,
        Y                   = -15020,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x516,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 42010,
        Z                   = 4250,
        Y                   = 48860,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x516,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -35030,
        TriggerZ            = 4000,
        TriggerY            = 5960,
        TriggerRange        = 5000,
        ActorX              = -31230,
        ActorZ              = 5500,
        ActorY              = 5960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -72130,
        TriggerZ            = 4000,
        TriggerY            = -77200,
        TriggerRange        = 1000,
        ActorX              = -71520,
        ActorZ              = 4000,
        ActorY              = -77200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41290,
        TriggerZ            = 4250,
        TriggerY            = -37040,
        TriggerRange        = 1000,
        ActorX              = 41910,
        ActorZ              = 4250,
        ActorY              = -37040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 55710,
        TriggerZ            = 4000,
        TriggerY            = 72760,
        TriggerRange        = 1000,
        ActorX              = 55970,
        ActorZ              = 4000,
        ActorY              = 73340,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2A2",          # 00, 0
        "Function_1_2D2",          # 01, 1
        "Function_2_33A",          # 02, 2
        "Function_3_4C6",          # 03, 3
        "Function_4_656",          # 04, 4
        "Function_5_74B",          # 05, 5
        "Function_6_7BF",          # 06, 6
        "Function_7_114E",         # 07, 7
        "Function_8_118D",         # 08, 8
        "Function_9_11D3",         # 09, 9
        "Function_10_1219",        # 0A, 10
        "Function_11_1244",        # 0B, 11
        "Function_12_12CA",        # 0C, 12
        "Function_13_135D",        # 0D, 13
    )


    def Function_0_2A2(): pass

    label("Function_0_2A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_2B3")
    OP_A3(0x10F0)
    Event(0, 5)
    Jump("loc_2D1")

    label("loc_2B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D1")
    SetMapFlags(0x10000000)
    Event(0, 6)

    label("loc_2D1")

    Return()

    # Function_0_2A2 end

    def Function_1_2D2(): pass

    label("Function_1_2D2")

    OP_16(0x2, 0xFA0, 0xFFFE36F8, 0xFFFDC998, 0x230074)
    OP_22(0x1C7, 0x0, 0x64)
    OP_71(0xA, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x464, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_300")
    OP_6F(0x7, 0)
    Jump("loc_307")

    label("loc_300")

    OP_6F(0x7, 60)

    label("loc_307")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x464, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_319")
    OP_6F(0x8, 0)
    Jump("loc_320")

    label("loc_319")

    OP_6F(0x8, 60)

    label("loc_320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x464, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_332")
    OP_6F(0x9, 0)
    Jump("loc_339")

    label("loc_332")

    OP_6F(0x9, 60)

    label("loc_339")

    Return()

    # Function_1_2D2 end

    def Function_2_33A(): pass

    label("Function_2_33A")

    OP_EA(0x2, 0xAF, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x464, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_412")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xC3, 1)"), scpexpr(EXPR_END)), "loc_3AB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xC3\x00\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2320)
    Jump("loc_40F")

    label("loc_3AB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xC3\x00\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xC3\x00\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_40F")

    Jump("loc_4B8")

    label("loc_412")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05At the bottom of the chest you find only crumbs.\x01",
            "Briefly wondering how long a chest like this\x01",
            "would keep food fresh for, you walk away.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4B8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_33A end

    def Function_3_4C6(): pass

    label("Function_3_4C6")

    OP_EA(0x2, 0xB0, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x464, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2A1, 1)"), scpexpr(EXPR_END)), "loc_537")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\xA1\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2321)
    Jump("loc_59B")

    label("loc_537")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\xA1\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xA1\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_59B")

    Jump("loc_648")

    label("loc_59E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05Despite your repeated searches, this chest\x01",
            "doesn't contain any invisible items. In fact,\x01",
            "it doesn't contain anything, visible or otherwise.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_648")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_4C6 end

    def Function_4_656(): pass

    label("Function_4_656")

    OP_EA(0x2, 0xB1, 0x1, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x464, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x1E)
    OP_73(0x9)
    OP_6F(0x9, 30)
    AddSepith(0x0, 0x64)
    AddSepith(0x1, 0x64)
    AddSepith(0x2, 0x64)
    AddSepith(0x3, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #6
        (
            "Found\x01",
            "#2C#56IEarth Sepith x100\x01",
            "#57IWater Sepith x100\x01",
            "#58IFire Sepith x100\x01",
            "#59IWind Sepith x100#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2322)
    Jump("loc_739")

    label("loc_71D")


    AnonymousTalk(    #7
        "\x07\x05Oh, no, not again...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_739")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_656 end

    def Function_5_74B(): pass

    label("Function_5_74B")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(40820, 4350, -31840, 0)
    OP_67(0, 7210, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(339000, 0)
    OP_6E(890, 0)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(2000)
    OP_22(0x7C, 0x0, 0x64)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_74B end

    def Function_6_7BF(): pass

    label("Function_6_7BF")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D6")
    Call(0, 11)
    Call(0, 12)

    label("loc_7D6")

    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-3530, 4350, -118640, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3730, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1E)
    OP_73(0x0)

    def lambda_848():
        OP_6D(-2020, 4000, -124090, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_848)
    OP_43(0x101, 0x1, 0x0, 0x7)
    Sleep(800)
    OP_43(0x102, 0x1, 0x0, 0x8)
    Sleep(800)
    OP_43(0xF8, 0x1, 0x0, 0x9)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0xA)
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #8
        0x101,
        "#1004F#6POh, wow!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        "#1044FIt's some kind of large plaza.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_11(0xAA, 0xC8, 0xFF, 0x0, 0x61A80, 0x0)
    OP_6D(-2020, 4000, -124090, 0)
    OP_67(0, 12070, -10000, 0)
    OP_6B(6250, 0)
    OP_6C(321000, 0)
    OP_6E(439, 0)

    def lambda_928():
        OP_6D(50600, 4000, -6600, 12000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_928)

    def lambda_940():
        OP_67(0, 8940, -10000, 12000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_940)

    def lambda_958():
        OP_6B(12250, 12000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_958)

    def lambda_968():
        OP_6C(338000, 12000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_968)

    def lambda_978():
        OP_6E(600, 12000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_978)
    OP_C8(0x200, 0x46, "C_PLAC27._CH", 0x0, 0xFA0)
    Sleep(2000)

    def lambda_9A2():
        OP_8E(0xFE, 0x137E, 0xFA0, 0xFFFE2988, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_9A2)
    Sleep(800)

    def lambda_9C2():
        OP_8E(0xFE, 0x184C, 0xFA0, 0xFFFE292E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9C2)
    Sleep(800)

    def lambda_9E2():
        OP_8E(0xFE, 0x1338, 0xFA0, 0xFFFE247E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 3, lambda_9E2)
    Sleep(800)

    def lambda_A02():
        OP_8E(0xFE, 0x1A68, 0xFA0, 0xFFFE233E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 3, lambda_A02)
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    Fade(500)
    OP_6F(0x0, 0)
    OP_11(0xAA, 0xC8, 0xFF, 0x124F8, 0x186A0, 0x0)
    OP_6D(4980, 4000, -120120, 0)
    OP_67(0, 5900, -10000, 0)
    OP_6B(3860, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0xF8, 0xFF)
    OP_44(0xF9, 0xFF)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    SetChrPos(0x101, 6250, 4000, -120500, 0)
    SetChrPos(0x102, 4950, 4000, -120500, 0)
    SetChrPos(0xF8, 6250, 4000, -121800, 0)
    SetChrPos(0xF9, 4950, 4000, -121800, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B42")

    ChrTalk(    #10
        0x102,
        (
            "#1044F#6PAnd there are massive buildings\x01",
            "as far as the eye can see.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CEA")

    label("loc_B42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B95")

    ChrTalk(    #11
        0x109,
        (
            "#1064F#6PAnd nothing but huge buildings\x01",
            "everywhere you look!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CEA")

    label("loc_B95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD2")

    ChrTalk(    #12
        0x103,
        "#023F#6PAnd the buildings are massive!\x02",
    )

    CloseMessageWindow()
    Jump("loc_CEA")

    label("loc_BD2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C19")

    ChrTalk(    #13
        0x106,
        "#052F#6PAnd the buildings are even bigger. Damn.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CEA")

    label("loc_C19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C6A")

    ChrTalk(    #14
        0x108,
        (
            "#073F#6PThe scale of the buildings is tremendous,\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CEA")

    label("loc_C6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CB3")

    ChrTalk(    #15
        0x104,
        (
            "#033F#6PAnd the buildings!\x01",
            "Such overwhelming size!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CEA")

    label("loc_CB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CEA")

    ChrTalk(    #16
        0x10B,
        "#213F#6PAnd the buildings are HUGE!\x02",
    )

    CloseMessageWindow()

    label("loc_CEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D4D")

    ChrTalk(    #17
        0x105,
        (
            "#1163F#6PThe roads are so broad and open, too.\x01",
            "I wonder what this place was.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F13")

    label("loc_D4D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DA5")

    ChrTalk(    #18
        0x10B,
        (
            "#212F#6PReally huge roads, too.\x01",
            "I wonder what this place was for.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F13")

    label("loc_DA5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E18")

    ChrTalk(    #19
        0x104,
        (
            "#035F#6PAnd the roads are broad and open.\x01",
            "What was this plaza used for, precisely,\x01",
            "I wonder.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F13")

    label("loc_E18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E7F")

    ChrTalk(    #20
        0x108,
        (
            "#073F#6PAnd the roads are quite large.\x01",
            "I do wonder what this place was\x01",
            "used for.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F13")

    label("loc_E7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EC7")

    ChrTalk(    #21
        0x106,
        "#555F#6PBig roads, too. Wonder what went on here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F13")

    label("loc_EC7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F13")

    ChrTalk(    #22
        0x103,
        (
            "#022F#6PAnd such wide roads.\x01",
            "I wonder what went on here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F13")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_104A")

    ChrTalk(    #23
        0x107,
        (
            "#560FI think...this was an industrial area\x01",
            "of some sort, maybe.\x02\x03",

            "It'd make sense if all this water\x01",
            "was for industrial use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x102,
        "#1040FI see, yes, that would make sense.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1016FYeah, it doesn't really feel like\x01",
            "some place you'd want to live in.\x02\x03",

            "#1006FAnyway, let's have a look around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1114")

    label("loc_104A")


    ChrTalk(    #26
        0x102,
        (
            "#1035FI think this may be an industrial area.\x02\x03",

            "#1040FIt would make sense if this water\x01",
            "is for industrial use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#1015FOh, I see. Yeah, that makes sense.\x02\x03",

            "#1006FAnyway, let's have a look around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1114")

    OP_A2(0x221E)
    OP_28(0x9E, 0x4, 0x2)
    OP_28(0x9E, 0x4, 0x8)

    def lambda_1127():
        OP_6B(4600, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1127)

    def lambda_1137():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1137)
    OP_30(0x0)
    WaitChrThread(0x101, 0x1)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_6_7BF end

    def Function_7_114E(): pass

    label("Function_7_114E")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -2120, 4350, -118450, 180)
    OP_8E(0xFE, 0xFFFFF7C2, 0xFA0, 0xFFFE1F38, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF7FE, 0xFA0, 0xFFFE16B4, 0x7D0, 0x0)
    Return()

    # Function_7_114E end

    def Function_8_118D(): pass

    label("Function_8_118D")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -2120, 4350, -118450, 180)
    OP_8E(0xFE, 0xFFFFF7C2, 0xFA0, 0xFFFE1F38, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFC68, 0xFA0, 0xFFFE1B1E, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_8_118D end

    def Function_9_11D3(): pass

    label("Function_9_11D3")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -2120, 4350, -118450, 180)
    OP_8E(0xFE, 0xFFFFF7C2, 0xFA0, 0xFFFE1F38, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF3E4, 0xFA0, 0xFFFE1BFA, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_9_11D3 end

    def Function_10_1219(): pass

    label("Function_10_1219")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -2120, 4350, -118450, 180)
    OP_8E(0xFE, 0xFFFFF7C2, 0xFA0, 0xFFFE1F38, 0x7D0, 0x0)
    Return()

    # Function_10_1219 end

    def Function_11_1244(): pass

    label("Function_11_1244")

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
        (0, "loc_12BD"),
        (1, "loc_12C3"),
        (SWITCH_DEFAULT, "loc_12C9"),
    )


    label("loc_12BD")

    OP_A2(0x1200)
    Jump("loc_12C9")

    label("loc_12C3")

    OP_A2(0x1201)
    Jump("loc_12C9")

    label("loc_12C9")

    Return()

    # Function_11_1244 end

    def Function_12_12CA(): pass

    label("Function_12_12CA")

    FadeToDark(0, 0, -1)
    OP_6D(-78410, -8000, -230560, 0)
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

    # Function_12_12CA end

    def Function_13_135D(): pass

    label("Function_13_135D")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #28
        "\x07\x05The gate is firmly locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_13_135D end

    SaveToFile()

Try(main)
