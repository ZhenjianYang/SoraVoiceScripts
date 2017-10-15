from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3511   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3511.x',
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
        'ED6_DT09/CH10710 ._CH',             # 00
        'ED6_DT09/CH10711 ._CH',             # 01
        'ED6_DT09/CH10720 ._CH',             # 02
        'ED6_DT09/CH10721 ._CH',             # 03
        'ED6_DT09/CH10730 ._CH',             # 04
        'ED6_DT09/CH10731 ._CH',             # 05
        'ED6_DT09/CH10740 ._CH',             # 06
        'ED6_DT09/CH10741 ._CH',             # 07
        'ED6_DT29/CH12140 ._CH',             # 08
        'ED6_DT29/CH12141 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT09/CH10710P._CP',             # 00
        'ED6_DT09/CH10711P._CP',             # 01
        'ED6_DT09/CH10720P._CP',             # 02
        'ED6_DT09/CH10721P._CP',             # 03
        'ED6_DT09/CH10730P._CP',             # 04
        'ED6_DT09/CH10731P._CP',             # 05
        'ED6_DT09/CH10740P._CP',             # 06
        'ED6_DT09/CH10741P._CP',             # 07
        'ED6_DT29/CH12140P._CP',             # 08
        'ED6_DT29/CH12141P._CP',             # 09
    )

    DeclActor(
        TriggerX            = -3400,
        TriggerZ            = 0,
        TriggerY            = -22930,
        TriggerRange        = 1000,
        ActorX              = -3400,
        ActorZ              = 0,
        ActorY              = -23590,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3430,
        TriggerZ            = 0,
        TriggerY            = -22930,
        TriggerRange        = 1000,
        ActorX              = 3490,
        ActorZ              = 0,
        ActorY              = -23630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4760,
        TriggerZ            = 0,
        TriggerY            = 22800,
        TriggerRange        = 1000,
        ActorX              = 4760,
        ActorZ              = 0,
        ActorY              = 23420,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4540,
        TriggerZ            = 0,
        TriggerY            = 22820,
        TriggerRange        = 1000,
        ActorX              = -4630,
        ActorZ              = 0,
        ActorY              = 23480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_18A",          # 00, 0
        "Function_1_18B",          # 01, 1
        "Function_2_1F0",          # 02, 2
        "Function_3_381",          # 03, 3
        "Function_4_4B4",          # 04, 4
        "Function_5_621",          # 05, 5
    )


    def Function_0_18A(): pass

    label("Function_0_18A")

    Return()

    # Function_0_18A end

    def Function_1_18B(): pass

    label("Function_1_18B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D")
    OP_6F(0x0, 0)
    Jump("loc_1A4")

    label("loc_19D")

    OP_6F(0x0, 60)

    label("loc_1A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B6")
    OP_6F(0x1, 0)
    Jump("loc_1BD")

    label("loc_1B6")

    OP_6F(0x1, 60)

    label("loc_1BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CF")
    OP_6F(0x2, 0)
    Jump("loc_1D6")

    label("loc_1CF")

    OP_6F(0x2, 60)

    label("loc_1D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E8")
    OP_6F(0x3, 0)
    Jump("loc_1EF")

    label("loc_1E8")

    OP_6F(0x3, 60)

    label("loc_1EF")

    Return()

    # Function_1_18B end

    def Function_2_1F0(): pass

    label("Function_2_1F0")

    OP_EA(0x2, 0xC7, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_261")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xFC\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1540)
    Jump("loc_2C5")

    label("loc_261")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xFC\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFC\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_2C5")

    Jump("loc_373")

    label("loc_2C8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05You wonder if you could use arts to turn this\x01",
            "chest into a small, wooden bathtub. Water would\x01",
            "probably be fine. Fire to heat it, likely not.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_373")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_1F0 end

    def Function_3_381(): pass

    label("Function_3_381")

    OP_EA(0x2, 0xC8, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_459")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_3F2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\xF6\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1541)
    Jump("loc_456")

    label("loc_3F2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\xF6\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF6\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_456")

    Jump("loc_4A6")

    label("loc_459")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05Orbmints: Keeping your breath fresher, longer.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4A6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_381 end

    def Function_4_4B4(): pass

    label("Function_4_4B4")

    OP_EA(0x2, 0xC9, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_525")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "Found \x1F\xFE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1542)
    Jump("loc_589")

    label("loc_525")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "Found \x1F\xFE\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFE\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_589")

    Jump("loc_613")

    label("loc_58C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x05 As you look into the darkness of the empty\x01",
            "chest, it reminds you of the darkness that fills\x01",
            "your heart.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_613")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_4B4 end

    def Function_5_621(): pass

    label("Function_5_621")

    OP_EA(0x2, 0xCA, 0x0, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_717")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x1E)
    OP_73(0x3)
    OP_6F(0x3, 30)
    AddSepith(0x0, 0x14)
    AddSepith(0x1, 0x14)
    AddSepith(0x2, 0x14)
    AddSepith(0x3, 0x14)
    AddSepith(0x4, 0x14)
    AddSepith(0x5, 0x14)
    AddSepith(0x6, 0x14)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #9
        (
            "Found\x01",
            "#2C#56IEarth Sepith\x01",
            "#57IWater Sepith\x01",
            "#58IFire Sepith\x01",
            "#59IWind Sepith\x01",
            "#62ITime Sepith\x01",
            "#60ISpace Sepith\x01",
            "#61IMirage Sepith x20#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1543)
    Jump("loc_74E")

    label("loc_717")


    AnonymousTalk(    #10
        "\x07\x05I gave you everything I had to give, and yet...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_74E")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_621 end

    SaveToFile()

Try(main)
