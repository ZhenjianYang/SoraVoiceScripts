from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C0703   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0703.x',
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


    DeclEvent(
        X                   = -3400,
        Y                   = -2000,
        Z                   = 56200,
        Range               = 3400,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xE09C,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )


    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 400,
        TriggerY            = 88300,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = 400,
        ActorY              = 89000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 400,
        TriggerY            = -88300,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = 400,
        ActorY              = -89000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 290,
        TriggerZ            = 0,
        TriggerY            = 45880,
        TriggerRange        = 1000,
        ActorX              = 230,
        ActorZ              = 800,
        ActorY              = 46150,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 46950,
        TriggerZ            = 0,
        TriggerY            = -1000,
        TriggerRange        = 1000,
        ActorX              = 47050,
        ActorZ              = 800,
        ActorY              = -840,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -46770,
        TriggerZ            = 0,
        TriggerY            = -750,
        TriggerRange        = 1000,
        ActorX              = -46750,
        ActorZ              = 800,
        ActorY              = -440,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -10,
        TriggerZ            = 0,
        TriggerY            = -47710,
        TriggerRange        = 1000,
        ActorX              = -60,
        ActorZ              = 800,
        ActorY              = -47460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1A2",          # 00, 0
        "Function_1_1ED",          # 01, 1
        "Function_2_26A",          # 02, 2
        "Function_3_3F7",          # 03, 3
        "Function_4_520",          # 04, 4
        "Function_5_989",          # 05, 5
        "Function_6_18F8",         # 06, 6
        "Function_7_1C76",         # 07, 7
        "Function_8_22A8",         # 08, 8
        "Function_9_2A09",         # 09, 9
        "Function_10_3335",        # 0A, 10
        "Function_11_33BB",        # 0B, 11
        "Function_12_344A",        # 0C, 12
        "Function_13_354A",        # 0D, 13
        "Function_14_35C2",        # 0E, 14
        "Function_15_36C2",        # 0F, 15
        "Function_16_3766",        # 10, 16
        "Function_17_3878",        # 11, 17
        "Function_18_38F9",        # 12, 18
        "Function_19_3A0B",        # 13, 19
        "Function_20_3A8C",        # 14, 20
        "Function_21_3B9E",        # 15, 21
        "Function_22_3C1F",        # 16, 22
        "Function_23_3D31",        # 17, 23
        "Function_24_3DB2",        # 18, 24
        "Function_25_3E91",        # 19, 25
        "Function_26_3F70",        # 1A, 26
        "Function_27_3FBE",        # 1B, 27
    )


    def Function_0_1A2(): pass

    label("Function_0_1A2")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_1C2"),
        (101, "loc_1C9"),
        (102, "loc_1D0"),
        (103, "loc_1D7"),
        (104, "loc_1DE"),
        (105, "loc_1E5"),
        (SWITCH_DEFAULT, "loc_1EC"),
    )


    label("loc_1C2")

    Event(0, 12)
    Jump("loc_1EC")

    label("loc_1C9")

    Event(0, 14)
    Jump("loc_1EC")

    label("loc_1D0")

    Event(0, 16)
    Jump("loc_1EC")

    label("loc_1D7")

    Event(0, 18)
    Jump("loc_1EC")

    label("loc_1DE")

    Event(0, 20)
    Jump("loc_1EC")

    label("loc_1E5")

    Event(0, 22)
    Jump("loc_1EC")

    label("loc_1EC")

    Return()

    # Function_0_1A2 end

    def Function_1_1ED(): pass

    label("Function_1_1ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FF")
    OP_6F(0x20, 0)
    Jump("loc_206")

    label("loc_1FF")

    OP_6F(0x20, 60)

    label("loc_206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_218")
    OP_6F(0x21, 0)
    Jump("loc_21F")

    label("loc_218")

    OP_6F(0x21, 60)

    label("loc_21F")

    LoadEffect(0x0, "map\\\\mp049_21.eff")
    LoadEffect(0x1, "map\\\\mp049_22.eff")
    Call(0, 4)
    OP_1B(0x0, 0x0, 0xD)
    OP_1B(0x1, 0x0, 0xF)
    OP_1B(0x2, 0x0, 0x11)
    OP_1B(0x3, 0x0, 0x13)
    OP_1B(0x4, 0x0, 0x15)
    OP_1B(0x5, 0x0, 0x17)
    Return()

    # Function_1_1ED end

    def Function_2_26A(): pass

    label("Function_2_26A")

    OP_EA(0x2, 0x1A, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_342")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x20, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x144, 1)"), scpexpr(EXPR_END)), "loc_2DB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x44\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F0A)
    Jump("loc_33F")

    label("loc_2DB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x44\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x44\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x20, 60)
    OP_70(0x20, 0x0)

    label("loc_33F")

    Jump("loc_3E9")

    label("loc_342")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05I once heard on the playground that if you check\x01",
            "a certain chest enough, it'll give you all the items\x01",
            "and as much mira as you can hold! \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3E9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_26A end

    def Function_3_3F7(): pass

    label("Function_3_3F7")

    OP_EA(0x2, 0x1B, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CF")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x21, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x16E, 1)"), scpexpr(EXPR_END)), "loc_468")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\x6E\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F0C)
    Jump("loc_4CC")

    label("loc_468")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\x6E\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x6E\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x21, 60)
    OP_70(0x21, 0x0)

    label("loc_4CC")

    Jump("loc_512")

    label("loc_4CF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05This chest is as empty as your soul.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_512")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_3F7 end

    def Function_4_520(): pass

    label("Function_4_520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C6, 1)), scpexpr(EXPR_END)), "loc_5A1")
    OP_72(0x8, 0x20)
    OP_72(0x9, 0x20)
    OP_72(0xA, 0x20)
    OP_72(0xB, 0x20)
    OP_72(0xC, 0x20)
    OP_72(0xD, 0x20)
    OP_72(0xE, 0x20)
    OP_72(0x8, 0x8)
    OP_72(0x9, 0x8)
    OP_72(0xA, 0x8)
    OP_72(0xB, 0x8)
    OP_72(0xC, 0x8)
    OP_72(0xD, 0x8)
    OP_72(0xE, 0x8)
    OP_6F(0x8, 360)
    OP_6F(0x9, 0)
    OP_6F(0xA, 0)
    OP_6F(0xB, 0)
    OP_6F(0xC, 0)
    OP_6F(0xD, 0)
    OP_6F(0xE, 0)
    Jump("loc_618")

    label("loc_5A1")

    OP_72(0x8, 0x20)
    OP_72(0x9, 0x20)
    OP_72(0xA, 0x20)
    OP_72(0xB, 0x20)
    OP_72(0xC, 0x20)
    OP_72(0xD, 0x20)
    OP_72(0xE, 0x20)
    OP_72(0x8, 0x8)
    OP_72(0x9, 0x8)
    OP_72(0xA, 0x8)
    OP_72(0xB, 0x8)
    OP_72(0xC, 0x8)
    OP_72(0xD, 0x8)
    OP_72(0xE, 0x8)
    OP_6F(0x8, 0)
    OP_6F(0x9, 0)
    OP_6F(0xA, 0)
    OP_6F(0xB, 0)
    OP_6F(0xC, 0)
    OP_6F(0xD, 0)
    OP_6F(0xE, 0)

    label("loc_618")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 7)), scpexpr(EXPR_END)), "loc_6AA")
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
    Jump("loc_732")

    label("loc_6AA")

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

    label("loc_732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 0)), scpexpr(EXPR_END)), "loc_7D5")
    OP_72(0xF, 0x20)
    OP_72(0x10, 0x20)
    OP_72(0x11, 0x20)
    OP_72(0x12, 0x20)
    OP_72(0x13, 0x20)
    OP_72(0x14, 0x20)
    OP_72(0x15, 0x20)
    OP_72(0x16, 0x20)
    OP_72(0x17, 0x20)
    OP_72(0xF, 0x8)
    OP_72(0x10, 0x8)
    OP_72(0x11, 0x8)
    OP_72(0x12, 0x8)
    OP_72(0x13, 0x8)
    OP_72(0x14, 0x8)
    OP_72(0x15, 0x8)
    OP_72(0x16, 0x8)
    OP_72(0x17, 0x8)
    OP_6F(0xF, 0)
    OP_6F(0x10, 0)
    OP_6F(0x11, 0)
    OP_6F(0x12, 0)
    OP_6F(0x13, 0)
    OP_6F(0x14, 360)
    OP_6F(0x15, 0)
    OP_6F(0x16, 0)
    OP_6F(0x17, 0)
    Jump("loc_86E")

    label("loc_7D5")

    OP_72(0xF, 0x20)
    OP_72(0x10, 0x20)
    OP_72(0x11, 0x20)
    OP_72(0x12, 0x20)
    OP_72(0x13, 0x20)
    OP_72(0x14, 0x20)
    OP_72(0x15, 0x20)
    OP_72(0x16, 0x20)
    OP_72(0x17, 0x20)
    OP_72(0xF, 0x8)
    OP_72(0x10, 0x8)
    OP_72(0x11, 0x8)
    OP_72(0x12, 0x8)
    OP_72(0x13, 0x8)
    OP_72(0x14, 0x8)
    OP_72(0x15, 0x8)
    OP_72(0x16, 0x8)
    OP_72(0x17, 0x8)
    OP_6F(0xF, 0)
    OP_6F(0x10, 0)
    OP_6F(0x11, 0)
    OP_6F(0x12, 0)
    OP_6F(0x13, 0)
    OP_6F(0x14, 0)
    OP_6F(0x15, 0)
    OP_6F(0x16, 0)
    OP_6F(0x17, 0)

    label("loc_86E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 1)), scpexpr(EXPR_END)), "loc_900")
    OP_72(0x18, 0x20)
    OP_72(0x19, 0x20)
    OP_72(0x1A, 0x20)
    OP_72(0x1B, 0x20)
    OP_72(0x1C, 0x20)
    OP_72(0x1D, 0x20)
    OP_72(0x1E, 0x20)
    OP_72(0x1F, 0x20)
    OP_72(0x18, 0x8)
    OP_72(0x19, 0x8)
    OP_72(0x1A, 0x8)
    OP_72(0x1B, 0x8)
    OP_72(0x1C, 0x8)
    OP_72(0x1D, 0x8)
    OP_72(0x1E, 0x8)
    OP_72(0x1F, 0x8)
    OP_6F(0x18, 360)
    OP_6F(0x19, 0)
    OP_6F(0x1A, 0)
    OP_6F(0x1B, 0)
    OP_6F(0x1C, 0)
    OP_6F(0x1D, 0)
    OP_6F(0x1E, 0)
    OP_6F(0x1F, 0)
    Jump("loc_988")

    label("loc_900")

    OP_72(0x18, 0x20)
    OP_72(0x19, 0x20)
    OP_72(0x1A, 0x20)
    OP_72(0x1B, 0x20)
    OP_72(0x1C, 0x20)
    OP_72(0x1D, 0x20)
    OP_72(0x1E, 0x20)
    OP_72(0x1F, 0x20)
    OP_72(0x18, 0x8)
    OP_72(0x19, 0x8)
    OP_72(0x1A, 0x8)
    OP_72(0x1B, 0x8)
    OP_72(0x1C, 0x8)
    OP_72(0x1D, 0x8)
    OP_72(0x1E, 0x8)
    OP_72(0x1F, 0x8)
    OP_6F(0x18, 0)
    OP_6F(0x19, 0)
    OP_6F(0x1A, 0)
    OP_6F(0x1B, 0)
    OP_6F(0x1C, 0)
    OP_6F(0x1D, 0)
    OP_6F(0x1E, 0)
    OP_6F(0x1F, 0)

    label("loc_988")

    Return()

    # Function_4_520 end

    def Function_5_989(): pass

    label("Function_5_989")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 6)), scpexpr(EXPR_END)), "loc_991")
    Return()

    label("loc_991")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9B6")
    Call(0, 10)
    Call(0, 11)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_9B6")

    Fade(500)
    OP_6D(-180, 400, 58250, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 1120, 400, 57110, 180)
    SetChrPos(0x102, -190, 400, 57080, 180)
    SetChrPos(0xF8, 1030, 400, 58470, 180)
    SetChrPos(0xF9, -230, 400, 58410, 180)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #6
        0x101,
        "#1004F#2PHey...\x02",
    )

    CloseMessageWindow()

    def lambda_A74():
        OP_6D(240, 400, 48840, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A74)

    def lambda_A8C():
        OP_67(0, 4080, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A8C)

    def lambda_AA4():
        OP_6B(3600, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AA4)

    def lambda_AB4():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_AB4)

    def lambda_AC4():
        OP_6E(290, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AC4)
    WaitChrThread(0x101, 0x0)

    def lambda_AD9():
        OP_8E(0xFE, 0x41A, 0xC8, 0xC404, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AD9)
    Sleep(300)

    def lambda_AF9():
        OP_8E(0xFE, 0xFFFFFF38, 0xC8, 0xC3BE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AF9)
    Sleep(100)

    def lambda_B19():
        OP_8E(0xFE, 0x3DE, 0x190, 0xC896, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_B19)
    Sleep(300)

    def lambda_B39():
        OP_8E(0xFE, 0xFFFFFE7A, 0x190, 0xC8F0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_B39)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    OP_6D(-890, 0, 45660, 0)
    OP_67(0, 5240, -10000, 0)
    OP_6B(3630, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 1040, 200, 43380, 0)
    SetChrPos(0x102, -180, 200, 43430, 0)
    SetChrPos(0xF8, 1360, 400, 41830, 0)
    SetChrPos(0xF9, -80, 400, 42080, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(200)

    ChrTalk(    #7
        0x101,
        (
            "#1015F#5PThis is...some sort of\x01",
            "computer thingy. I think?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CA2")

    ChrTalk(    #8
        0x109,
        (
            "#1064FHmmmm, looks like some\x01",
            "sorta computer terminal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE7")

    label("loc_CA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CE7")

    ChrTalk(    #9
        0x107,
        (
            "#064FI think it's some kind of\x01",
            "computer terminal!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CE7")


    ChrTalk(    #10
        0x102,
        "#1040F#5PLet's have a look.\x02",
    )

    CloseMessageWindow()

    def lambda_D0E():
        OP_6D(-140, 400, 46050, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D0E)
    OP_8F(0x102, 0xFA, 0x96, 0xB22A, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #11
        0x102,
        (
            "#1035F#6PHmmmm...\x02\x03",

            "#1040FThis should work.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x9C, 0x0, 0x64)
    OP_B0(0x8, 0x78)
    OP_70(0x8, 0x168)
    Sleep(2500)
    OP_22(0x9D, 0x0, 0x64)
    OP_B0(0x9, 0x64)
    OP_B0(0xD, 0x64)
    OP_B0(0xE, 0x64)
    OP_70(0x9, 0xF0)
    Sleep(100)
    OP_70(0xD, 0xF0)
    Sleep(100)
    OP_70(0xE, 0xF0)
    Sleep(100)
    OP_22(0xB9, 0x0, 0x64)

    def lambda_DC3():
        OP_6D(-970, 890, 46970, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DC3)

    def lambda_DDB():
        OP_67(0, 4420, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DDB)

    def lambda_DF3():
        OP_6B(3790, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DF3)

    def lambda_E03():
        OP_6E(274, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E03)
    OP_B0(0xA, 0x64)
    OP_B0(0xB, 0x64)
    OP_B0(0xC, 0x64)
    OP_70(0xA, 0x168)
    OP_70(0xB, 0x168)
    OP_70(0xC, 0x168)
    OP_73(0xA)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #12
        0x101,
        "#1004FWaaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x102,
        (
            "#1040F#5PIt does seem to be some sort of computer\x01",
            "terminal for viewing information.\x02\x03",

            "Let's have a look at the contents.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #14
        (
            "\x07\x05#1S[Concerning the Seal Mechanism 1/4]\x01",
            "My name is Celeste D. Auslese.\x01",
            "I am t■ de■■■er of ■ Seal M■■sm, and ■■\x01",
            "man ulti■■■■■y re■■■■e ■ th■ ■■■ing of\x01",
            "the A■■■■. I h■■ de■■■ed to ■■■■ b■■■ a\x01",
            "■■■■ of ■■■■ds for ■■■ ■■■■ to come ■ c■■\x01",
            "the S■■■■ ■■al is a■■■■ed and ■■ ■■■ole,\x01",
            "■■■■h we ■■■■■ in ■■■er d■■■■n, s■■■■ld\x01",
            "■■■■■■■ to re■■■.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #15
        (
            "\x07\x05#1SIf y■u wh■ r■■d th■ me■■ge ■■■ to\x01",
            "pr■■■■t the ■■■■■■■'s ■■■■rn, I ■■■■ th■■\x01",
            "in■■■■■ion will ■■■ y■u. Ho■■■■r, if y■u ■■■■\x01",
            "to r■■■ore the Au■■■■, I beg y■u, ■■■■■■■er.\x01",
            "The ■■■■■■■'s p■w■r is t■■ gr■■t f■r we Children\x01",
            "of Man t■ w■■■d. When we ■■■■ it, it l■■ ■■ ■■■o\x01",
            "the ■■■■■st Gehenna.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #16
        "\x07\x00Received #1021i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3FD, 1)
    OP_A2(0x1E31)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_137B")

    ChrTalk(    #17
        0x101,
        (
            "#1019FWhat the heck good is this? It's basically\x01",
            "unreadable except for the beginning.\x02\x03",

            "#1004FThough...that 'Auslese' bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x105,
        (
            "#047FYes... It is the name of\x01",
            "the royal family of Liberl.\x02\x03",

            "#040FThis may have been written by\x01",
            "someone connected to us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C5")

    label("loc_137B")


    ChrTalk(    #19
        0x101,
        (
            "#1019FWhat the heck good is that? It's\x01",
            "unreadable except for the beginning.\x02\x03",

            "#1004FThough...that 'Auslese' bit.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_145D")

    ChrTalk(    #20
        0x103,
        (
            "#023FAuslese is the name of\x01",
            "Liberl's royal family.\x02\x03",

            "#020FThey may be related, somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C5")

    label("loc_145D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14CA")

    ChrTalk(    #21
        0x106,
        (
            "#053FAuslese's the name of the\x01",
            "Liberlian royal family.\x02\x03",

            "#051FMight be related somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C5")

    label("loc_14CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1554")

    ChrTalk(    #22
        0x108,
        (
            "#073FUnless I'm mistaken, Auslese is the\x01",
            "name of the Liberlian royal family, yes?\x02\x03",

            "#070FThis person may be related.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C5")

    label("loc_1554")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15C5")

    ChrTalk(    #23
        0x109,
        (
            "#1060FYeah, Auslese is the name\x01",
            "of Liberl's royal family.\x02\x03",

            "#1065FBet they're related somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15C5")

    OP_8C(0x102, 180, 400)

    ChrTalk(    #24
        0x102,
        (
            "#1035F#2PThat's true...\x02\x03",

            "#1043FIt is possible that there's a connection there.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17C7")

    ChrTalk(    #25
        0x101,
        "#1007FYeah, maybe. Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x107,
        "#064F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#1015F#2PTita? What's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x107,
        (
            "#061FOh, um!\x02\x03",

            "#560FI was just thinking that the crystal\x01",
            "looks a lot like a quartz circuit!\x02\x03",

            "I think...maybe, if we have time,\x01",
            "we can repair it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        "#1004F#2PReally?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x107,
        (
            "#560FI think so!\x02\x03",

            "I know Grandpa's used Capel to\x01",
            "repair quartz circuits before!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        (
            "#1040F#2PIn that case, we should get\x01",
            "this to the professor at once.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1816")

    label("loc_17C7")


    ChrTalk(    #32
        0x101,
        (
            "#1007FYeah, maybe.\x02\x03",

            "#1006FWell, it could be useful,\x01",
            "so we should take it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1816")

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
    OP_6D(580, 200, 43320, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 580, 200, 43320, 0)
    SetChrPos(0x1, 580, 200, 43320, 0)
    SetChrPos(0x2, 580, 200, 43320, 0)
    SetChrPos(0x3, 580, 200, 43320, 0)
    OP_69(0x0, 0x0)
    OP_A2(0x1E06)
    Sleep(500)
    FadeToBright(1000, 0)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_5_989 end

    def Function_6_18F8(): pass

    label("Function_6_18F8")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #33
        (
            "\x07\x05#1S[Concerning the Seal Mechanism 1/4]\x01",
            "My name is Celeste D. Auslese.\x01",
            "I am t■ de■■■er of ■ Seal M■■sm, and ■■\x01",
            "man ulti■■■■■y re■■■■e ■ th■ ■■■ing of\x01",
            "the A■■■■. I h■■ de■■■ed to ■■■■ b■■■ a\x01",
            "■■■■ of ■■■■ds for ■■■ ■■■■ to come ■ c■■\x01",
            "the S■■■■ ■■al is a■■■■ed and ■■ ■■■ole,\x01",
            "■■■■h we ■■■■■ in ■■■er d■■■■n, s■■■■ld\x01",
            "■■■■■■■ to re■■■.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #34
        (
            "\x07\x05#1SIf y■u wh■ r■■d th■ me■■ge ■■■ to\x01",
            "pr■■■■t the ■■■■■■■'s ■■■■rn, I ■■■■ th■■\x01",
            "in■■■■■ion will ■■■ y■u. Ho■■■■r, if y■u ■■■■\x01",
            "to r■■■ore the Au■■■■, I beg y■u, ■■■■■■■er.\x01",
            "The ■■■■■■■'s p■w■r is t■■ gr■■t f■r we Children\x01",
            "of Man t■ w■■■d. When we ■■■■ it, it l■■ ■■ ■■■o\x01",
            "the ■■■■■st Gehenna.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Return()

    # Function_6_18F8 end

    def Function_7_1C76(): pass

    label("Function_7_1C76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_205F")
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

    AnonymousTalk(    #35
        (
            "\x07\x05#1S[Concerning the Seal Mechanism 2/4]\x01",
            "The purp■se ■f the s■■■s is to pr■■■ent any\x01",
            "c■ntact betw■■n the A■■■■e and hu■■■■y, thus\x01",
            "ens■ring ■■■■ity's ■■■■■■. I fe■l the n■ed t■\x01",
            "clari■■: the A■■■■■, its■lf, d■es n■t ■■■■ t■\x01",
            "c■■■■■l or ha■m huma■■■■. The di■■■■■ that\x01",
            "■■■■■ed us was ■ur f■■lt al■ne.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #36
        (
            "\x07\x05#1SDo n■t ■■■■ the merc■ of ■ur great\x01",
            "G■ddess in g■■■■ng t■■s gift t■ ■■.\x01",
            "It ■■ we wh■ ■re ■■equal t■ s■ch a g■■■.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #37
        "\x07\x00Received #1022i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3FE, 1)
    OP_A2(0x1E07)
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
    OP_6D(47020, 0, -2740, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 47020, 0, -2740, 0)
    SetChrPos(0x1, 47020, 0, -2740, 0)
    SetChrPos(0x2, 47020, 0, -2740, 0)
    SetChrPos(0x3, 47020, 0, -2740, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Jump("loc_22A4")

    label("loc_205F")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #38
        (
            "\x07\x05#1S[Concerning the Seal Mechanism 2/4]\x01",
            "The purp■se ■f the s■■■s is to pr■■■ent any\x01",
            "c■ntact betw■■n the A■■■■e and hu■■■■y, thus\x01",
            "ens■ring ■■■■ity's ■■■■■■. I fe■l the n■ed t■\x01",
            "clari■■: the A■■■■■, its■lf, d■es n■t ■■■■ t■\x01",
            "c■■■■■l or ha■m huma■■■■. The di■■■■■ that\x01",
            "■■■■■ed us was ■ur f■■lt al■ne.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #39
        (
            "\x07\x05#1SDo n■t ■■■■ the merc■ of ■ur great\x01",
            "G■ddess in g■■■■ng t■■s gift t■ ■■.\x01",
            "It ■■ we wh■ ■re ■■equal t■ s■ch a g■■■.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_22A4")

    TalkEnd(0xFF)
    Return()

    # Function_7_1C76 end

    def Function_8_22A8(): pass

    label("Function_8_22A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2734")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    OP_B0(0x14, 0x78)
    OP_70(0x14, 0x168)
    Sleep(2500)
    OP_22(0x9D, 0x0, 0x64)
    OP_B0(0x12, 0x64)
    OP_B0(0x13, 0x64)
    OP_B0(0x15, 0x64)
    OP_B0(0x16, 0x64)
    OP_B0(0x17, 0x64)
    OP_70(0x12, 0xF0)
    Sleep(100)
    OP_70(0x13, 0xF0)
    Sleep(100)
    OP_70(0x15, 0xF0)
    Sleep(100)
    OP_70(0x16, 0xF0)
    Sleep(100)
    OP_70(0x17, 0xF0)
    Sleep(100)
    OP_22(0xB9, 0x0, 0x64)
    OP_B0(0xF, 0x64)
    OP_B0(0x10, 0x64)
    OP_B0(0x11, 0x64)
    OP_70(0xF, 0x168)
    OP_70(0x10, 0x168)
    OP_70(0x11, 0x168)
    OP_73(0xF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #40
        (
            "\x07\x05#1S[Concerning the Seal Mechanism 3/4]\x01",
            "In tr■th, the c■■stru■■■ion and imp■■■ntati■■ of\x01",
            "the s■■■ goes dir■■■ly ■■■■nst th■ wi■■ ■f the\x01",
            "p■■■le and ■ur de■■■atic ide■■s. Ev■n am■■■ ■ur\x01",
            "g■■■p, s■me be■■■ed we sh■■■ try t■ ■■■ a w■■\x01",
            "t■ use th■ ■■■■■■'s p■w■r e■■■■■ly.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #41
        (
            "\x07\x05#1SH■wev■■, ■nce it ■bt■■■■d auto■■my, the\x01",
            "■■■■■■e be■■n to c■■■■■ ■ur s■■■■ty and ■■r ■■■■es\x01",
            "dras■■cally. It d■■ n■t just ■■■■ern its■■f w■th\x01",
            "■■r ph■■■■al w■ll-■■■ng; it ■■■■idered our ■■■tal\x01",
            "■■■■■■■■■ t■ be ■ t■p ■■■■■ity as w■ll.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #42
        "\x07\x00Received #1023i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3FF, 1)
    OP_A2(0x1E08)
    Sleep(100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0xF, 0)
    OP_6F(0x10, 0)
    OP_6F(0x11, 0)
    OP_6F(0x12, 0)
    OP_6F(0x13, 0)
    OP_6F(0x14, 360)
    OP_6F(0x15, 0)
    OP_6F(0x16, 0)
    OP_6F(0x17, 0)
    OP_6D(-46490, 200, -3220, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -46490, 200, -3220, 0)
    SetChrPos(0x1, -46490, 200, -3220, 0)
    SetChrPos(0x2, -46490, 200, -3220, 0)
    SetChrPos(0x3, -46490, 200, -3220, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Jump("loc_2A05")

    label("loc_2734")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #43
        (
            "\x07\x05#1S[Concerning the Seal Mechanism 3/4]\x01",
            "In tr■th, the c■■stru■■■ion and imp■■■ntati■■ of\x01",
            "the s■■■ goes dir■■■ly ■■■■nst th■ wi■■ ■f the\x01",
            "p■■■le and ■ur de■■■atic ide■■s. Ev■n am■■■ ■ur\x01",
            "g■■■p, s■me be■■■ed we sh■■■ try t■ ■■■ a w■■\x01",
            "t■ use th■ ■■■■■■'s p■w■r e■■■■■ly.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #44
        (
            "\x07\x05#1SH■wev■■, ■nce it ■bt■■■■d auto■■my, the\x01",
            "■■■■■■e be■■n to c■■■■■ ■ur s■■■■ty and ■■r ■■■■es\x01",
            "dras■■cally. It d■■ n■t just ■■■■ern its■■f w■th\x01",
            "■■r ph■■■■al w■ll-■■■ng; it ■■■■idered our ■■■tal\x01",
            "■■■■■■■■■ t■ be ■ t■p ■■■■■ity as w■ll.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2A05")

    TalkEnd(0xFF)
    Return()

    # Function_8_22A8 end

    def Function_9_2A09(): pass

    label("Function_9_2A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F6F")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    OP_B0(0x18, 0x78)
    OP_70(0x18, 0x168)
    Sleep(2500)
    OP_22(0x9D, 0x0, 0x64)
    OP_B0(0x1C, 0x64)
    OP_B0(0x1D, 0x64)
    OP_B0(0x1E, 0x64)
    OP_B0(0x1F, 0x64)
    OP_70(0x1C, 0xF0)
    Sleep(100)
    OP_70(0x1D, 0xF0)
    Sleep(100)
    OP_70(0x1E, 0xF0)
    Sleep(100)
    OP_70(0x1F, 0xF0)
    Sleep(500)
    OP_22(0xB9, 0x0, 0x64)
    OP_B0(0x19, 0x64)
    OP_B0(0x1A, 0x64)
    OP_B0(0x1B, 0x64)
    OP_70(0x19, 0x168)
    OP_70(0x1A, 0x168)
    OP_70(0x1B, 0x168)
    OP_73(0x19)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #45
        (
            "\x07\x05#1S[Concerning the Seal Mechanism 4/4]\x01",
            "To pr■vide an ■■■■ple: the A■■■■■ faci■■■■■■d\x01",
            "the cre■■■■n ■f vi■■■■al rea■■■ies int■■ded t■\x01",
            "■■■uce eu■■■■a in pa■■■■ip■■ts. It ■ven a■t■■ed\x01",
            "b■■■n che■■stry to ■■■■eve th■s. It was n■\x01",
            "di■■er■nt than t■■■■g a p■■■■ful ■■■■■ric\x01",
            "st■■ulant and ■■■■■■inog■n at the ■■■■ time.\x01",
            "W■rse ■■ill, th■■■ ■■re n■ side ef■■■■s.\x01",
            "No phy■■■■■ o■■s, at le■st.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #46
        (
            "\x07\x05#1SSuch 'b■■ns' have br■■■ght hum■■ity's very\x01",
            "co■■■■■d exi■■■nce int■ que■■■■on. The eff■■■ts\x01",
            "already begin t■ tell up■■ ■ur citi■■■ry, and we\x01",
            "have preci■■s littl■ time l■ft t■ us.\x01",
            "As a res■lt, we fe■ have ove■■■me our di■■■■■■■■\x01",
            "t■ unde■■■■■e th■ Sealing--the te■■■ble ■■■■ we\x01",
            "had pre■■■■d sh■■ld a s■tu■■on like th■s ever\x01",
            "arise.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #47
        "\x07\x00Received #1024i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x400, 1)
    OP_A2(0x1E09)
    Sleep(100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x18, 360)
    OP_6F(0x19, 0)
    OP_6F(0x1A, 0)
    OP_6F(0x1B, 0)
    OP_6F(0x1C, 0)
    OP_6F(0x1D, 0)
    OP_6F(0x1E, 0)
    OP_6F(0x1F, 0)
    OP_6D(340, 200, -50000, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 340, 200, -50000, 0)
    SetChrPos(0x1, 340, 200, -50000, 0)
    SetChrPos(0x2, 340, 200, -50000, 0)
    SetChrPos(0x3, 340, 200, -50000, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Jump("loc_3331")

    label("loc_2F6F")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #48
        (
            "\x07\x05#1S[Concerning the Seal Mechanism 4/4]\x01",
            "To pr■vide an ■■■■ple: the A■■■■■ faci■■■■■■d\x01",
            "the cre■■■■n ■f vi■■■■al rea■■■ies int■■ded t■\x01",
            "■■■uce eu■■■■a in pa■■■■ip■■ts. It ■ven a■t■■ed\x01",
            "b■■■n che■■stry to ■■■■eve th■s. It was n■\x01",
            "di■■er■nt than t■■■■g a p■■■■ful ■■■■■ric\x01",
            "st■■ulant and ■■■■■■inog■n at the ■■■■ time.\x01",
            "W■rse ■■ill, th■■■ ■■re n■ side ef■■■■s.\x01",
            "No phy■■■■■ o■■s, at le■st.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #49
        (
            "\x07\x05#1SSuch 'b■■ns' have br■■■ght hum■■ity's very\x01",
            "co■■■■■d exi■■■nce int■ que■■■■on. The eff■■■ts\x01",
            "already begin t■ tell up■■ ■ur citi■■■ry, and we\x01",
            "have preci■■s littl■ time l■ft t■ us.\x01",
            "As a res■lt, we fe■ have ove■■■me our di■■■■■■■■\x01",
            "t■ unde■■■■■e th■ Sealing--the te■■■ble ■■■■ we\x01",
            "had pre■■■■d sh■■ld a s■tu■■on like th■s ever\x01",
            "arise.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3331")

    TalkEnd(0xFF)
    Return()

    # Function_9_2A09 end

    def Function_10_3335(): pass

    label("Function_10_3335")

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
        (0, "loc_33AE"),
        (1, "loc_33B4"),
        (SWITCH_DEFAULT, "loc_33BA"),
    )


    label("loc_33AE")

    OP_A2(0x1200)
    Jump("loc_33BA")

    label("loc_33B4")

    OP_A2(0x1201)
    Jump("loc_33BA")

    label("loc_33BA")

    Return()

    # Function_10_3335 end

    def Function_11_33BB(): pass

    label("Function_11_33BB")

    FadeToDark(0, 0, -1)
    OP_6D(-33260, 200, 68720, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_11_33BB end

    def Function_12_344A(): pass

    label("Function_12_344A")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 250, 81590, 0)
    SetChrPos(0x101, 500, 250, 81090, 180)
    SetChrPos(0x102, -500, 250, 81090, 180)
    SetChrPos(0xF8, 500, 250, 82090, 180)
    SetChrPos(0xF9, -500, 250, 82090, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 24)
    Call(0, 26)
    Fade(500)
    OP_6D(0, 300, 78810, 0)
    SetChrPos(0x0, 0, 300, 78810, 180)
    SetChrPos(0x1, 0, 300, 78810, 180)
    SetChrPos(0x2, 0, 300, 78810, 180)
    SetChrPos(0x3, 0, 300, 78810, 180)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_12_344A end

    def Function_13_354A(): pass

    label("Function_13_354A")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 250, 81590, 0)
    SetChrPos(0x101, -500, 250, 82090, 0)
    SetChrPos(0x102, 500, 250, 82090, 0)
    SetChrPos(0xF8, -500, 250, 81090, 0)
    SetChrPos(0xF9, 500, 250, 81090, 0)
    OP_0D()
    Call(0, 24)
    Call(0, 27)
    NewScene("ED6_DT21/C0702   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_13_354A end

    def Function_14_35C2(): pass

    label("Function_14_35C2")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(15310, -9350, 15430, 0)
    SetChrPos(0x101, 15810, -9350, 14930, 180)
    SetChrPos(0x102, 14810, -9350, 14930, 180)
    SetChrPos(0xF8, 15810, -9350, 15930, 180)
    SetChrPos(0xF9, 14810, -9350, 15930, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 24)
    Call(0, 26)
    Fade(500)
    OP_6D(15150, -9300, 12650, 0)
    SetChrPos(0x0, 15150, -9300, 12650, 180)
    SetChrPos(0x1, 15150, -9300, 12650, 180)
    SetChrPos(0x2, 15150, -9300, 12650, 180)
    SetChrPos(0x3, 15150, -9300, 12650, 180)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_14_35C2 end

    def Function_15_36C2(): pass

    label("Function_15_36C2")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(15310, -9350, 15430, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 14810, -9350, 15930, 0)
    SetChrPos(0x102, 15810, -9350, 15930, 0)
    SetChrPos(0xF8, 14810, -9350, 14930, 0)
    SetChrPos(0xF9, 15810, -9350, 14930, 0)
    OP_0D()
    Call(0, 24)
    Call(0, 27)
    NewScene("ED6_DT21/C0702   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_15_36C2 end

    def Function_16_3766(): pass

    label("Function_16_3766")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-15300, -9350, -15300, 0)
    OP_6C(225000, 0)
    SetChrPos(0x101, -15810, -9350, -14800, 0)
    SetChrPos(0x102, -14810, -9350, -14800, 0)
    SetChrPos(0xF8, -15810, -9350, -15800, 0)
    SetChrPos(0xF9, -14810, -9350, -15800, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 24)
    Call(0, 26)
    Fade(500)
    OP_6D(-15320, -9650, -10940, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0, -15320, -9650, -10940, 0)
    SetChrPos(0x1, -15320, -9650, -10940, 0)
    SetChrPos(0x2, -15320, -9650, -10940, 0)
    SetChrPos(0x3, -15320, -9650, -10940, 0)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_16_3766 end

    def Function_17_3878(): pass

    label("Function_17_3878")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-15300, -9350, -15300, 0)
    OP_6C(225000, 0)
    SetChrPos(0x101, -14810, -9350, -15800, 180)
    SetChrPos(0x102, -15810, -9350, -15800, 180)
    SetChrPos(0xF8, -14810, -9350, -14800, 180)
    SetChrPos(0xF9, -15810, -9350, -14800, 180)
    OP_0D()
    Call(0, 24)
    Call(0, 27)
    NewScene("ED6_DT21/C0702   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_17_3878 end

    def Function_18_38F9(): pass

    label("Function_18_38F9")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 250, -81500, 0)
    OP_6C(225000, 0)
    SetChrPos(0x101, -500, 250, -81000, 0)
    SetChrPos(0x102, 500, 250, -81000, 0)
    SetChrPos(0xF8, -500, 250, -82000, 0)
    SetChrPos(0xF9, 500, 250, -82000, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 25)
    Call(0, 26)
    Fade(500)
    OP_6D(40, -50, -77230, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0, 40, -50, -77230, 0)
    SetChrPos(0x1, 40, -50, -77230, 0)
    SetChrPos(0x2, 40, -50, -77230, 0)
    SetChrPos(0x3, 40, -50, -77230, 0)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_18_38F9 end

    def Function_19_3A0B(): pass

    label("Function_19_3A0B")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 250, -81500, 0)
    OP_6C(225000, 0)
    SetChrPos(0x101, 500, 250, -82000, 180)
    SetChrPos(0x102, -500, 250, -82000, 180)
    SetChrPos(0xF8, 500, 250, -81000, 180)
    SetChrPos(0xF9, -500, 250, -81000, 180)
    OP_0D()
    Call(0, 25)
    Call(0, 27)
    NewScene("ED6_DT21/C0704   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_19_3A0B end

    def Function_20_3A8C(): pass

    label("Function_20_3A8C")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(15000, -5750, -15500, 0)
    OP_6C(225000, 0)
    SetChrPos(0x101, 14500, -5750, -15000, 0)
    SetChrPos(0x102, 15500, -5750, -15000, 0)
    SetChrPos(0xF8, 14500, -5750, -16000, 0)
    SetChrPos(0xF9, 15500, -5750, -16000, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 25)
    Call(0, 26)
    Fade(500)
    OP_6D(15170, -6050, -11100, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0, 15170, -6050, -11100, 0)
    SetChrPos(0x1, 15170, -6050, -11100, 0)
    SetChrPos(0x2, 15170, -6050, -11100, 0)
    SetChrPos(0x3, 15170, -6050, -11100, 0)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_20_3A8C end

    def Function_21_3B9E(): pass

    label("Function_21_3B9E")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(15000, -5750, -15500, 0)
    OP_6C(225000, 0)
    SetChrPos(0x101, 15500, -5750, -16000, 180)
    SetChrPos(0x102, 14500, -5750, -16000, 180)
    SetChrPos(0xF8, 15500, -5750, -15000, 180)
    SetChrPos(0xF9, 14500, -5750, -15000, 180)
    OP_0D()
    Call(0, 25)
    Call(0, 27)
    NewScene("ED6_DT21/C0704   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_21_3B9E end

    def Function_22_3C1F(): pass

    label("Function_22_3C1F")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-15300, -5750, 15500, 0)
    OP_6C(315000, 0)
    SetChrPos(0x101, -14800, -5750, 15000, 180)
    SetChrPos(0x102, -15800, -5750, 15000, 180)
    SetChrPos(0xF8, -14800, -5750, 16000, 180)
    SetChrPos(0xF9, -15800, -5750, 16000, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 25)
    Call(0, 26)
    Fade(500)
    OP_6D(-15280, -5720, 12800, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0, -15280, -5720, 12800, 180)
    SetChrPos(0x1, -15280, -5720, 12800, 180)
    SetChrPos(0x2, -15280, -5720, 12800, 180)
    SetChrPos(0x3, -15280, -5720, 12800, 180)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_22_3C1F end

    def Function_23_3D31(): pass

    label("Function_23_3D31")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-15300, -5750, 15500, 0)
    OP_6C(315000, 0)
    SetChrPos(0x101, -15800, -5750, 16000, 0)
    SetChrPos(0x102, -14800, -5750, 16000, 0)
    SetChrPos(0xF8, -15800, -5750, 15000, 0)
    SetChrPos(0xF9, -14800, -5750, 15000, 0)
    OP_0D()
    Call(0, 25)
    Call(0, 27)
    NewScene("ED6_DT21/C0704   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_23_3D31 end

    def Function_24_3DB2(): pass

    label("Function_24_3DB2")

    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_24_3DB2 end

    def Function_25_3E91(): pass

    label("Function_25_3E91")

    PlayEffect(0x1, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_25_3E91 end

    def Function_26_3F70(): pass

    label("Function_26_3F70")


    def lambda_3F76():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3F76)

    def lambda_3F88():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3F88)

    def lambda_3F9A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3F9A)

    def lambda_3FAC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3FAC)
    Sleep(2500)
    Return()

    # Function_26_3F70 end

    def Function_27_3FBE(): pass

    label("Function_27_3FBE")


    def lambda_3FC4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3FC4)

    def lambda_3FD6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3FD6)

    def lambda_3FE8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3FE8)

    def lambda_3FFA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3FFA)
    Sleep(2000)
    Return()

    # Function_27_3FBE end

    SaveToFile()

Try(main)
