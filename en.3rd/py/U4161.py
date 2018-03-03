from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U4161   ._SN',
        MapName             = 'gaiden2',
        Location            = 'U4161.x',
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
        TriggerX            = 124330,
        TriggerZ            = 0,
        TriggerY            = 67840,
        TriggerRange        = 1000,
        ActorX              = 124330,
        ActorZ              = 1000,
        ActorY              = 67840,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -6220,
        TriggerZ            = 0,
        TriggerY            = 61170,
        TriggerRange        = 1000,
        ActorX              = -6220,
        ActorZ              = 1000,
        ActorY              = 61170,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_F2",           # 00, 0
        "Function_1_F3",           # 01, 1
        "Function_2_126",          # 02, 2
        "Function_3_274",          # 03, 3
    )


    def Function_0_F2(): pass

    label("Function_0_F2")

    Return()

    # Function_0_F2 end

    def Function_1_F3(): pass

    label("Function_1_F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_105")
    OP_6F(0xD, 0)
    Jump("loc_10C")

    label("loc_105")

    OP_6F(0xD, 60)

    label("loc_10C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11E")
    OP_6F(0xE, 0)
    Jump("loc_125")

    label("loc_11E")

    OP_6F(0xE, 60)

    label("loc_125")

    Return()

    # Function_1_F3 end

    def Function_2_126(): pass

    label("Function_2_126")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E4")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xD, 0x1E)
    OP_73(0xD)
    OP_6F(0xD, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0x32)
    AddSepith(0x1, 0x32)
    AddSepith(0x2, 0x32)
    AddSepith(0x3, 0x32)

    AnonymousTalk(    #0
        (
            "\x07\x02Obtained:\x01",
            "#56IEarth Sepith x50\x01",
            "#57IWater Sepith x50\x01",
            "#58IFire Sepith x50\x01",
            "#59IWind Sepith x50.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x27BC)
    Jump("loc_25D")

    label("loc_1E4")


    AnonymousTalk(    #1
        (
            "\x07\x05You don't understand! I coulda had items. I coulda been a treasure.\x01",
            "I could've been something...instead of empty.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_25D")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x121, 0x0)
    Return()

    # Function_2_126 end

    def Function_3_274(): pass

    label("Function_3_274")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_332")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xE, 0x1E)
    OP_73(0xE)
    OP_6F(0xE, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0x32)
    AddSepith(0x1, 0x32)
    AddSepith(0x2, 0x32)
    AddSepith(0x3, 0x32)

    AnonymousTalk(    #2
        (
            "\x07\x02Obtained:\x01",
            "#56IEarth Sepith x50\x01",
            "#57IWater Sepith x50\x01",
            "#58IFire Sepith x50\x01",
            "#59IWind Sepith x50.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x27BD)
    Jump("loc_40B")

    label("loc_332")


    AnonymousTalk(    #3
        (
            "\x07\x05Did you know? Trails in the Sky takes place in Liberl, but there are other\x01",
            "Trails games that take place beyond the kingdom's borders. For example,\x01",
            "Trails of Cold Steel happens in the Erebonian Empire (buy it).\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_40B")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x122, 0x0)
    Return()

    # Function_3_274 end

    SaveToFile()

Try(main)
