from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C2209   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2209.x',
        MapIndex            = 84,
        MapDefaultBGM       = "ed60015",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/C2209   ._SN',
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
        'Manoria Byroad',                       # 9
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


    DeclNpc(
        X                   = 1330,
        Z                   = -430,
        Y                   = -46450,
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


    DeclActor(
        TriggerX            = -960,
        TriggerZ            = 25000,
        TriggerY            = -770,
        TriggerRange        = 800,
        ActorX              = -960,
        ActorZ              = 26500,
        ActorY              = -770,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_EE",           # 00, 0
        "Function_1_EF",           # 01, 1
        "Function_2_119",          # 02, 2
        "Function_3_120",          # 03, 3
        "Function_4_127",          # 04, 4
    )


    def Function_0_EE(): pass

    label("Function_0_EE")

    Return()

    # Function_0_EE end

    def Function_1_EF(): pass

    label("Function_1_EF")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFDDD20, 0x230050)
    OP_B0(0x0, 0x78)
    OP_B0(0x1, 0x78)
    OP_1C(0x0, 0x0, 0x2)
    OP_1C(0x1, 0x0, 0x3)
    OP_22(0x1C5, 0x1, 0x64)
    Return()

    # Function_1_EF end

    def Function_2_119(): pass

    label("Function_2_119")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_2_119 end

    def Function_3_120(): pass

    label("Function_3_120")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_3_120 end

    def Function_4_127(): pass

    label("Function_4_127")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        (
            "\x07\x05 　　　Danger!　　　\x01",
            "※Unauthorized personnel prohibited\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_4_127 end

    SaveToFile()

Try(main)
