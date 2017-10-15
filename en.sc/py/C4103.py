from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'C4103   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4103.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60021",
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
        'Erbe Scenic Route',                    # 9
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
        X                   = 267460,
        Z                   = 0,
        Y                   = -13160,
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
        TriggerX            = 309300,
        TriggerZ            = -70,
        TriggerY            = 19380,
        TriggerRange        = 1000,
        ActorX              = 314040,
        ActorZ              = -1000,
        ActorY              = 19290,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_EE",           # 00, 0
        "Function_1_EF",           # 01, 1
        "Function_2_10C",          # 02, 2
    )


    def Function_0_EE(): pass

    label("Function_0_EE")

    Return()

    # Function_0_EE end

    def Function_1_EF(): pass

    label("Function_1_EF")

    OP_16(0x2, 0xFA0, 0x2BF20, 0xFFFE1F88, 0x230066)
    OP_22(0x1CC, 0x1, 0x64)
    OP_22(0x1C7, 0x1, 0x64)
    Return()

    # Function_1_EF end

    def Function_2_10C(): pass

    label("Function_2_10C")

    EventBegin(0x1)

    ChrTalk(    #0
        0x101,
        "#1001FI bet I could fish here!\x02",
    )

    CloseMessageWindow()

    def lambda_138():
        OP_6D(312040, -50, 18590, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_138)

    def lambda_150():
        OP_67(0, 9500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_150)

    def lambda_168():
        OP_6B(3200, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_168)

    def lambda_178():
        OP_6C(315000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_178)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x05Try fishing?\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Hook, Line, and Sinker\x01",      # 0
            "Spare the Rod\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21E")
    OP_C0(0xE, 0x28, 0x4B834, 0xFFFFFFBA, 0x4BB4, 0x5A, 0x4CAB8, 0xFFFFFFBA, 0x4B5A)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_22D")

    label("loc_21E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22D")
    EventEnd(0x1)

    label("loc_22D")

    Return()

    # Function_2_10C end

    SaveToFile()

Try(main)
