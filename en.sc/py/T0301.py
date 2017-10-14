from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0301   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0301.x',
        MapIndex            = 15,
        MapDefaultBGM       = "ed60084",
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
        'Elize Highway',                        # 9
    )

    DeclEntryPoint(
        Unknown_00              = 2000,
        Unknown_04              = 0,
        Unknown_08              = -6000,
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
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 9600,
        Unknown_04              = 875,
        Unknown_08              = 300,
        Unknown_0C              = 4,
        Unknown_0E              = 118,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 9600,
        Unknown_04              = 875,
        Unknown_08              = 300,
        Unknown_0C              = 4,
        Unknown_0E              = 118,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 9600,
        Unknown_04              = 875,
        Unknown_08              = 300,
        Unknown_0C              = 4,
        Unknown_0E              = 118,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    DeclNpc(
        X                   = 4110,
        Z                   = -1000,
        Y                   = -46140,
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


    ScpFunction(
        "Function_0_196",          # 00, 0
        "Function_1_1D7",          # 01, 1
        "Function_2_1F0",          # 02, 2
        "Function_3_2BE",          # 03, 3
    )


    def Function_0_196(): pass

    label("Function_0_196")

    OP_16(0x2, 0xFA0, 0xFFFE17B8, 0xFFFDF878, 0x230003)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_1BE")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 2)
    Jump("loc_1D6")

    label("loc_1BE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D6")
    Event(0, 3)

    label("loc_1D6")

    Return()

    # Function_0_196 end

    def Function_1_1D7(): pass

    label("Function_1_1D7")

    SetMapFlags(0x10)
    OP_11(0x4B, 0x4B, 0x96, 0x0, 0xEA60, 0x0)
    OP_82(0x80, 0x2)
    Return()

    # Function_1_1D7 end

    def Function_2_1F0(): pass

    label("Function_2_1F0")

    EventBegin(0x0)
    OP_11(0x4B, 0x4B, 0x96, 0x0, 0x11170, 0x0)
    OP_6D(-9230, 0, 8720, 0)
    OP_67(0, 9280, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(39000, 0)
    OP_6E(334, 0)
    FadeToBright(2000, 0)

    def lambda_24E():
        OP_6D(4580, 450, 4260, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24E)

    def lambda_266():
        OP_67(0, 7240, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_266)
    OP_6C(25000, 8000)

    def lambda_287():
        OP_6B(3500, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_287)

    def lambda_297():
        OP_6E(275, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_297)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0311   ._SN", 107, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1F0 end

    def Function_3_2BE(): pass

    label("Function_3_2BE")

    EventBegin(0x0)
    SetChrPos(0x101, -1820, 3450, 860, 270)
    OP_6D(-3930, 3450, 850, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_72(0x2, 0x10)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x3B)
    OP_73(0x2)
    Sleep(500)
    OP_8E(0x101, 0xFFFFF196, 0xD7A, 0x438, 0x5DC, 0x0)
    OP_72(0x2, 0x800)
    OP_6F(0x2, 59)
    OP_70(0x2, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)

    def lambda_368():
        OP_6D(-6160, 3450, 1600, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_368)
    OP_8E(0x101, 0xFFFFE6A6, 0xD7A, 0x686, 0x5DC, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    OP_71(0x2, 0x800)

    ChrTalk(    #0
        0x101,
        (
            "#1335F*sigh* The fog's still really crazy.\x02\x03",

            "#452F...\x02",
        )
    )

    CloseMessageWindow()
    OP_AD(0x2400C3, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    Sleep(2000)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)
    Sleep(500)

    ChrTalk(    #1
        0x101,
        "#1336FAnyway, let's check the first floor.\x02",
    )

    CloseMessageWindow()
    OP_71(0x2, 0x10)
    OP_A2(0x1818)
    EventEnd(0x0)
    Return()

    # Function_3_2BE end

    SaveToFile()

Try(main)
