from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U4120   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4120.x',
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


    DeclActor(
        TriggerX            = 117490,
        TriggerZ            = 0,
        TriggerY            = 3960,
        TriggerRange        = 1000,
        ActorX              = 116610,
        ActorZ              = 1000,
        ActorY              = 4230,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -70,
        TriggerZ            = 0,
        TriggerY            = 129500,
        TriggerRange        = 1000,
        ActorX              = -780,
        ActorZ              = 1000,
        ActorY              = 129490,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_F2",           # 00, 0
        "Function_1_F3",           # 01, 1
        "Function_2_142",          # 02, 2
        "Function_3_31C",          # 03, 3
    )


    def Function_0_F2(): pass

    label("Function_0_F2")

    Return()

    # Function_0_F2 end

    def Function_1_F3(): pass

    label("Function_1_F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E4, 1)), scpexpr(EXPR_END)), "loc_106")
    OP_B1("U4120_y")
    Jump("loc_10F")

    label("loc_106")

    OP_B1("U4120_n")

    label("loc_10F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121")
    OP_6F(0x3, 0)
    Jump("loc_128")

    label("loc_121")

    OP_6F(0x3, 60)

    label("loc_128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13A")
    OP_6F(0x4, 0)
    Jump("loc_141")

    label("loc_13A")

    OP_6F(0x4, 60)

    label("loc_141")

    Return()

    # Function_1_F3 end

    def Function_2_142(): pass

    label("Function_2_142")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x259, 1)"), scpexpr(EXPR_END)), "loc_1B0")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x59\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2787)
    Jump("loc_218")

    label("loc_1B0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\x59\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x59\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_218")

    Jump("loc_30E")

    label("loc_21B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05[12/36] The place looked less like a shop and more like the newest\x01",
            "secret playground for the local children, long abandoned after the\x01",
            "passing of its owner. But no; to clarify, it was very much 'in business.'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xFB, 0x0)

    label("loc_30E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_142 end

    def Function_3_31C(): pass

    label("Function_3_31C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x4A0, 1)"), scpexpr(EXPR_END)), "loc_38A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\xA0\x04\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2784)
    Jump("loc_3F2")

    label("loc_38A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\xA0\x04\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xA0\x04\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_3F2")

    Jump("loc_4F6")

    label("loc_3F5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05[17/36] 'Good riddance,' the son coldly muttered as he turned the key to\x01",
            "lock the shop. This would be the last time he would be forced to ever\x01",
            "step inside. 'I'll bet I can fetch a pretty mira for his tools at the market.'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xFC, 0x0)

    label("loc_4F6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_31C end

    SaveToFile()

Try(main)
