from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4123   ._SN',
        MapName             = 'gaiden2',
        Location            = 'U4123.x',
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
        TriggerX            = 117130,
        TriggerZ            = 0,
        TriggerY            = -1810,
        TriggerRange        = 1000,
        ActorX              = 116000,
        ActorZ              = 3000,
        ActorY              = -1500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -6080,
        TriggerZ            = 0,
        TriggerY            = -90,
        TriggerRange        = 1000,
        ActorX              = -6080,
        ActorZ              = 1000,
        ActorY              = -90,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_F2",           # 00, 0
        "Function_1_106",          # 01, 1
        "Function_2_11D",          # 02, 2
        "Function_3_191",          # 03, 3
        "Function_4_332",          # 04, 4
        "Function_5_3E8",          # 05, 5
        "Function_6_493",          # 06, 6
    )


    def Function_0_F2(): pass

    label("Function_0_F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_105")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_105")

    Return()

    # Function_0_F2 end

    def Function_1_106(): pass

    label("Function_1_106")

    OP_82(0x80, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_119")
    OP_82(0x81, 0x0)
    Jump("loc_11C")

    label("loc_119")

    OP_82(0x82, 0x0)

    label("loc_11C")

    Return()

    # Function_1_106 end

    def Function_2_11D(): pass

    label("Function_2_11D")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05打开『门』吗？\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_17A")

    label("loc_17A")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_2_11D end

    def Function_3_191(): pass

    label("Function_3_191")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, 119150, 0, -1320, 270)
    SetChrPos(0x1, 119160, 0, -2640, 270)
    SetChrPos(0x2, 120770, 0, -1370, 270)
    SetChrPos(0x3, 121190, 0, -2760, 270)
    OP_6D(117190, 0, -1720, 0)
    OP_67(0, 4270, -10000, 0)
    OP_6B(3690, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_267")
    OP_28(0x4, 0x4, 0x2)
    OP_82(0x81, 0x2)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_267")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #1
        (
            "\x07\x05#40W　 汝须将银发之华丽舞者\x01",
            "　　  引领至吾面前。\x01",
            "#500W\x01",
            "#40W   如此，则『门』将开启……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_326")
    Call(0, 2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_323")
    Call(0, 4)

    label("loc_323")

    Jump("loc_326")

    label("loc_326")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_3_191 end

    def Function_4_332(): pass

    label("Function_4_332")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x6, 0)
    OP_70(0x6, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x6)
    Sleep(500)

    def lambda_39B():
        OP_6B(2750, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_39B)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_E3(0x0, 0x7, 0, 0x0)
    NewScene("ED6_DT21/P9000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_332 end

    def Function_5_3E8(): pass

    label("Function_5_3E8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, 119150, 0, -1320, 270)
    SetChrPos(0x1, 119160, 0, -2640, 270)
    SetChrPos(0x2, 120770, 0, -1370, 270)
    SetChrPos(0x3, 121190, 0, -2760, 270)
    OP_6D(117190, 0, -1720, 0)
    OP_67(0, 4270, -10000, 0)
    OP_6B(3690, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_5_3E8 end

    def Function_6_493(): pass

    label("Function_6_493")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #2
        "\x07\x05导力通讯似乎无法使用。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_6_493 end

    SaveToFile()

Try(main)
