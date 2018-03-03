from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2810   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2810.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60183",
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
            'ED6_DT21/SUB000  ._SN',
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
        TriggerX            = 51020,
        TriggerZ            = 0,
        TriggerY            = 31860,
        TriggerRange        = 800,
        ActorX              = 51020,
        ActorZ              = 1500,
        ActorY              = 31860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 51030,
        TriggerZ            = 0,
        TriggerY            = 2090,
        TriggerRange        = 400,
        ActorX              = 51030,
        ActorZ              = 800,
        ActorY              = 2090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 59060,
        TriggerZ            = 0,
        TriggerY            = 2090,
        TriggerRange        = 400,
        ActorX              = 59060,
        ActorZ              = 800,
        ActorY              = 2090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_116",          # 00, 0
        "Function_1_117",          # 01, 1
        "Function_2_137",          # 02, 2
        "Function_3_18F",          # 03, 3
        "Function_4_1DC",          # 04, 4
    )


    def Function_0_116(): pass

    label("Function_0_116")

    Return()

    # Function_0_116 end

    def Function_1_117(): pass

    label("Function_1_117")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_136")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_136")
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_72(0x1004, 0x0)
    ExitThread()

    label("loc_136")

    Return()

    # Function_1_117 end

    def Function_2_137(): pass

    label("Function_2_137")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        "\x07\x05Quiet in the halls! --Student Council\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_2_137 end

    def Function_3_18F(): pass

    label("Function_3_18F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A7")

    ChrTalk(    #1
        0x105,
        "#047F...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D8")

    label("loc_1A7")


    ChrTalk(    #2
        0x105,
        (
            "#047F...\x02\x03",

            "I've got no reason to be here.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1D8")

    TalkEnd(0xFF)
    Return()

    # Function_3_18F end

    def Function_4_1DC(): pass

    label("Function_4_1DC")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #3
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_4_1DC end

    SaveToFile()

Try(main)
