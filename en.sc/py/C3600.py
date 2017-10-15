from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3600   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3600.x',
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


    DeclActor(
        TriggerX            = 30,
        TriggerZ            = -7650,
        TriggerY            = -710,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = -7650,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4990,
        TriggerZ            = -7200,
        TriggerY            = -5010,
        TriggerRange        = 1000,
        ActorX              = -5460,
        ActorZ              = -7200,
        ActorY              = -5470,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -7190,
        TriggerZ            = -7200,
        TriggerY            = 10,
        TriggerRange        = 1000,
        ActorX              = -7810,
        ActorZ              = -7200,
        ActorY              = 10,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4970,
        TriggerZ            = -7200,
        TriggerY            = 5030,
        TriggerRange        = 1000,
        ActorX              = -5440,
        ActorZ              = -7200,
        ActorY              = 5500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5020,
        TriggerZ            = -7200,
        TriggerY            = 4990,
        TriggerRange        = 1000,
        ActorX              = 5450,
        ActorZ              = -7200,
        ActorY              = 5430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7200,
        TriggerZ            = -7200,
        TriggerY            = 10,
        TriggerRange        = 1000,
        ActorX              = 7860,
        ActorZ              = -7200,
        ActorY              = 10,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4990,
        TriggerZ            = -7200,
        TriggerY            = -5020,
        TriggerRange        = 1000,
        ActorX              = 5520,
        ActorZ              = -7200,
        ActorY              = -5550,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1A6",          # 00, 0
        "Function_1_1C5",          # 01, 1
        "Function_2_2A7",          # 02, 2
        "Function_3_3CE",          # 03, 3
        "Function_4_548",          # 04, 4
        "Function_5_676",          # 05, 5
        "Function_6_7A2",          # 06, 6
        "Function_7_924",          # 07, 7
        "Function_8_A4B",          # 08, 8
        "Function_9_BA7",          # 09, 9
        "Function_10_D8D",         # 0A, 10
        "Function_11_DF8",         # 0B, 11
        "Function_12_E63",         # 0C, 12
        "Function_13_ECE",         # 0D, 13
        "Function_14_F39",         # 0E, 14
        "Function_15_101F",        # 0F, 15
        "Function_16_10A4",        # 10, 16
        "Function_17_1129",        # 11, 17
        "Function_18_11AE",        # 12, 18
        "Function_19_1233",        # 13, 19
        "Function_20_132E",        # 14, 20
        "Function_21_13A6",        # 15, 21
        "Function_22_1485",        # 16, 22
        "Function_23_1564",        # 17, 23
        "Function_24_15B2",        # 18, 24
    )


    def Function_0_1A6(): pass

    label("Function_0_1A6")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_1B6"),
        (101, "loc_1BD"),
        (SWITCH_DEFAULT, "loc_1C4"),
    )


    label("loc_1B6")

    Event(0, 9)
    Jump("loc_1C4")

    label("loc_1BD")

    Event(0, 19)
    Jump("loc_1C4")

    label("loc_1C4")

    Return()

    # Function_0_1A6 end

    def Function_1_1C5(): pass

    label("Function_1_1C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D7")
    OP_6F(0x1, 0)
    Jump("loc_1DE")

    label("loc_1D7")

    OP_6F(0x1, 60)

    label("loc_1DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F0")
    OP_6F(0x2, 0)
    Jump("loc_1F7")

    label("loc_1F0")

    OP_6F(0x2, 60)

    label("loc_1F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_209")
    OP_6F(0x3, 0)
    Jump("loc_210")

    label("loc_209")

    OP_6F(0x3, 60)

    label("loc_210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_222")
    OP_6F(0x4, 0)
    Jump("loc_229")

    label("loc_222")

    OP_6F(0x4, 60)

    label("loc_229")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23B")
    OP_6F(0x5, 0)
    Jump("loc_242")

    label("loc_23B")

    OP_6F(0x5, 60)

    label("loc_242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_254")
    OP_6F(0x6, 0)
    Jump("loc_25B")

    label("loc_254")

    OP_6F(0x6, 60)

    label("loc_25B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26D")
    OP_6F(0x7, 0)
    Jump("loc_274")

    label("loc_26D")

    OP_6F(0x7, 60)

    label("loc_274")

    LoadEffect(0x0, "map\\\\mp049_21.eff")
    LoadEffect(0x1, "map\\\\mp049_22.eff")
    OP_1B(0x0, 0x0, 0xE)
    OP_1B(0x1, 0x0, 0x14)
    Return()

    # Function_1_1C5 end

    def Function_2_2A7(): pass

    label("Function_2_2A7")

    OP_EA(0x2, 0xD5, 0x0, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x1E)
    OP_73(0x1)
    OP_6F(0x1, 30)
    AddSepith(0x2, 0x12C)
    AddSepith(0x4, 0x64)
    AddSepith(0x5, 0x64)
    AddSepith(0x6, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        (
            "Found\x01",
            "#2C#58IFire Sepith x300\x01",
            "#62ITime Sepith x100\x01",
            "#60ISpace Sepith x100\x01",
            "#61IMirage Sepith x100#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1F20)
    Jump("loc_3BC")

    label("loc_36F")


    AnonymousTalk(    #1
        (
            "\x07\x05You have returned. The pact is sealed.\x01",
            "Your first born child is mine.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_3BC")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_2A7 end

    def Function_3_3CE(): pass

    label("Function_3_3CE")

    OP_EA(0x2, 0xD6, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_43F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "Found \x1F\xFC\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F22)
    Jump("loc_4A3")

    label("loc_43F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "Found \x1F\xFC\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFC\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_4A3")

    Jump("loc_53A")

    label("loc_4A6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05There's nothing in this chest, but you looked so\x01",
            "excited to open it that I didn't have the heart to\x01",
            "tell you earlier.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_53A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_3CE end

    def Function_4_548(): pass

    label("Function_4_548")

    OP_EA(0x2, 0xD7, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_620")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x200, 1)"), scpexpr(EXPR_END)), "loc_5B9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "Found \x1F\x00\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F23)
    Jump("loc_61D")

    label("loc_5B9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "Found \x1F\x00\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x00\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_61D")

    Jump("loc_668")

    label("loc_620")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05Everything that mattered in here is gone.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_668")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_548 end

    def Function_5_676(): pass

    label("Function_5_676")

    OP_EA(0x2, 0xD8, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_6E7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "Found \x1F\xFE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F24)
    Jump("loc_74B")

    label("loc_6E7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "Found \x1F\xFE\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFE\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_74B")

    Jump("loc_794")

    label("loc_74E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05Nooo! Give it back! That was my spleen!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_794")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_676 end

    def Function_6_7A2(): pass

    label("Function_6_7A2")

    OP_EA(0x2, 0xD9, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_813")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        "Found \x1F\xF8\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F25)
    Jump("loc_877")

    label("loc_813")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "Found \x1F\xF8\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF8\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_877")

    Jump("loc_916")

    label("loc_87A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "\x07\x05You open the chest to find a message scrawled\x01",
            "in blood along the underside of the lid:\x01",
            "'WHOEVER TOOK MY STUFF WILL PAY.' Huh.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_916")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_7A2 end

    def Function_7_924(): pass

    label("Function_7_924")

    OP_EA(0x2, 0xDA, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FC")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_995")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #14
        "Found \x1F\x02\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F26)
    Jump("loc_9F9")

    label("loc_995")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "Found \x1F\x02\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x02\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_9F9")

    Jump("loc_A3D")

    label("loc_9FC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x05You find only a bleak, empty void.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A3D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_924 end

    def Function_8_A4B(): pass

    label("Function_8_A4B")

    OP_EA(0x2, 0xDB, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B23")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_ABC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "Found \x1F\xFD\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F27)
    Jump("loc_B20")

    label("loc_ABC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "Found \x1F\xFD\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFD\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_B20")

    Jump("loc_B99")

    label("loc_B23")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "\x07\x05You open the chest, realize you already looted it,\x01",
            "then angrily slam the lid back down.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B99")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_A4B end

    def Function_9_BA7(): pass

    label("Function_9_BA7")

    EventBegin(0x0)
    OP_6D(680, 750, -84120, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(3460, 0)
    OP_6C(140000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 0, 1050, -83970, 0)
    SetChrPos(0x102, 0, 1050, -83970, 0)
    SetChrPos(0xF8, 0, 1050, -83970, 0)
    SetChrPos(0xF9, 0, 1050, -83970, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0xF8, 0x4)
    SetChrFlags(0xF9, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0xF8, 0x1)
    ClearChrFlags(0xF9, 0x1)
    OP_C8(0x200, 0x46, "C_PLAC22._CH", 0x0, 0x1F4)
    OP_DE("Carnelia Tower")
    FadeToBright(1000, 0)
    OP_43(0x101, 0x0, 0x0, 0xA)
    Sleep(800)

    def lambda_CBE():
        OP_6D(140, 600, -78810, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_CBE)
    OP_43(0x102, 0x0, 0x0, 0xB)
    Sleep(800)
    OP_43(0xF8, 0x0, 0x0, 0xC)
    Sleep(800)
    OP_43(0xF9, 0x0, 0x0, 0xD)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0xF8, 0x0)
    WaitChrThread(0xF9, 0x0)
    Fade(500)
    OP_6D(610, 600, -77870, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 610, 600, -77870, 0)
    SetChrPos(0x1, 610, 600, -77870, 0)
    SetChrPos(0x2, 610, 600, -77870, 0)
    SetChrPos(0x3, 610, 600, -77870, 0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_9_BA7 end

    def Function_10_D8D(): pass

    label("Function_10_D8D")


    def lambda_D93():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D93)

    def lambda_DAD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DAD)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_DD8():
        OP_8F(0xFE, 0x262, 0x258, 0xFFFECFD2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DD8)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_10_D8D end

    def Function_11_DF8(): pass

    label("Function_11_DF8")


    def lambda_DFE():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DFE)

    def lambda_E18():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E18)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_E43():
        OP_8F(0xFE, 0xFFFFFE2A, 0x258, 0xFFFECEF6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E43)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_11_DF8 end

    def Function_12_E63(): pass

    label("Function_12_E63")


    def lambda_E69():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E69)

    def lambda_E83():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E83)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_EAE():
        OP_8F(0xFE, 0x276, 0x2EE, 0xFFFECA32, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EAE)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_12_E63 end

    def Function_13_ECE(): pass

    label("Function_13_ECE")


    def lambda_ED4():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_ED4)

    def lambda_EEE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EEE)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_F19():
        OP_8F(0xFE, 0xFFFFFDE4, 0x2EE, 0xFFFECA28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F19)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_13_ECE end

    def Function_14_F39(): pass

    label("Function_14_F39")

    EventBegin(0x0)
    Fade(500)
    ClearMapFlags(0x1)
    OP_6D(680, 750, -84120, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(3460, 0)
    OP_6C(140000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 680, 700, -81310, 180)
    SetChrPos(0x102, -330, 700, -81100, 180)
    SetChrPos(0xF8, 910, 750, -79600, 180)
    SetChrPos(0xF9, -270, 750, -79450, 180)
    OP_43(0x101, 0x0, 0x0, 0xF)
    Sleep(300)
    OP_43(0x102, 0x0, 0x0, 0x10)
    Sleep(300)
    OP_43(0xF8, 0x0, 0x0, 0x11)
    Sleep(300)
    OP_43(0xF9, 0x0, 0x0, 0x12)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0xF8, 0x0)
    WaitChrThread(0xF9, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x2000000)
    NewScene("ED6_DT21/R3104   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_14_F39 end

    def Function_15_101F(): pass

    label("Function_15_101F")

    OP_91(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_1064():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1064)

    def lambda_107E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_107E)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_15_101F end

    def Function_16_10A4(): pass

    label("Function_16_10A4")

    OP_91(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_10E9():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10E9)

    def lambda_1103():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1103)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_16_10A4 end

    def Function_17_1129(): pass

    label("Function_17_1129")

    OP_91(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_116E():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_116E)

    def lambda_1188():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1188)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_17_1129 end

    def Function_18_11AE(): pass

    label("Function_18_11AE")

    OP_91(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_11F3():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11F3)

    def lambda_120D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_120D)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_18_11AE end

    def Function_19_1233(): pass

    label("Function_19_1233")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 250, 84530, 0)
    SetChrPos(0x101, 500, 250, 84030, 180)
    SetChrPos(0x102, -500, 250, 84030, 180)
    SetChrPos(0xF8, 500, 250, 85030, 180)
    SetChrPos(0xF9, -500, 250, 85030, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 22)
    Call(0, 23)
    Fade(500)
    OP_6D(-130, 250, 82150, 0)
    SetChrPos(0x0, -130, 250, 82150, 180)
    SetChrPos(0x1, -130, 250, 82150, 180)
    SetChrPos(0x2, -130, 250, 82150, 180)
    SetChrPos(0x3, -130, 250, 82150, 180)
    EventEnd(0x0)
    Return()

    # Function_19_1233 end

    def Function_20_132E(): pass

    label("Function_20_132E")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 250, 84530, 0)
    SetChrPos(0x101, -500, 250, 85030, 0)
    SetChrPos(0x102, 500, 250, 85030, 0)
    SetChrPos(0xF8, -500, 250, 84030, 0)
    SetChrPos(0xF9, 500, 250, 84030, 0)
    OP_0D()
    Call(0, 22)
    Call(0, 24)
    NewScene("ED6_DT21/C3601   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_132E end

    def Function_21_13A6(): pass

    label("Function_21_13A6")

    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_21_13A6 end

    def Function_22_1485(): pass

    label("Function_22_1485")

    PlayEffect(0x1, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_22_1485 end

    def Function_23_1564(): pass

    label("Function_23_1564")


    def lambda_156A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_156A)

    def lambda_157C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_157C)

    def lambda_158E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_158E)

    def lambda_15A0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_15A0)
    Sleep(2500)
    Return()

    # Function_23_1564 end

    def Function_24_15B2(): pass

    label("Function_24_15B2")


    def lambda_15B8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_15B8)

    def lambda_15CA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_15CA)

    def lambda_15DC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_15DC)

    def lambda_15EE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_15EE)
    Sleep(2000)
    Return()

    # Function_24_15B2 end

    SaveToFile()

Try(main)
