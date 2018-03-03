from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U2600   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U2600.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60231",
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
        TriggerX            = 32500,
        TriggerZ            = 1000,
        TriggerY            = 14500,
        TriggerRange        = 1000,
        ActorX              = 32500,
        ActorZ              = 1000,
        ActorY              = 14500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 23000,
        TriggerZ            = 6000,
        TriggerY            = 22500,
        TriggerRange        = 1000,
        ActorX              = 23000,
        ActorZ              = 6000,
        ActorY              = 22500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -35740,
        TriggerZ            = 1000,
        TriggerY            = 28720,
        TriggerRange        = 1000,
        ActorX              = -35740,
        ActorZ              = 1000,
        ActorY              = 28720,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 23090,
        TriggerZ            = 5000,
        TriggerY            = 32259,
        TriggerRange        = 1000,
        ActorX              = 23000,
        ActorZ              = 8000,
        ActorY              = 33000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_13A",          # 00, 0
        "Function_1_14E",          # 01, 1
        "Function_2_1C2",          # 02, 2
        "Function_3_39E",          # 03, 3
        "Function_4_575",          # 04, 4
        "Function_5_6E6",          # 05, 5
        "Function_6_73F",          # 06, 6
        "Function_7_92B",          # 07, 7
        "Function_8_9E1",          # 08, 8
    )


    def Function_0_13A(): pass

    label("Function_0_13A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_14D")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 8)

    label("loc_14D")

    Return()

    # Function_0_13A end

    def Function_1_14E(): pass

    label("Function_1_14E")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE61F0, 0x23004E)
    OP_82(0x80, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_173")
    OP_82(0x81, 0x0)
    Jump("loc_176")

    label("loc_173")

    OP_82(0x82, 0x0)

    label("loc_176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x575, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_188")
    OP_6F(0x2, 0)
    Jump("loc_18F")

    label("loc_188")

    OP_6F(0x2, 60)

    label("loc_18F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x575, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A1")
    OP_6F(0x3, 0)
    Jump("loc_1A8")

    label("loc_1A1")

    OP_6F(0x3, 60)

    label("loc_1A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x575, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BA")
    OP_6F(0x4, 0)
    Jump("loc_1C1")

    label("loc_1BA")

    OP_6F(0x4, 60)

    label("loc_1C1")

    Return()

    # Function_1_14E end

    def Function_2_1C2(): pass

    label("Function_2_1C2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x575, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x55A, 1)"), scpexpr(EXPR_END)), "loc_230")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x5A\x05\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BA8)
    Jump("loc_298")

    label("loc_230")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\x5A\x05\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x5A\x05\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_298")

    Jump("loc_390")

    label("loc_29B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05[36/36] That was how Jubilee, who adored her grandfather and took\x01",
            "every chance to spend her days with him as a child, became the new\x01",
            "owner of a little carpentry shop on Bose. [Trails in the Chest, Pt. I, END?]\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xF1, 0x0)

    label("loc_390")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_1C2 end

    def Function_3_39E(): pass

    label("Function_3_39E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x575, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_477")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x172, 1)"), scpexpr(EXPR_END)), "loc_40C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\x72\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BA9)
    Jump("loc_474")

    label("loc_40C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\x72\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x72\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_474")

    Jump("loc_567")

    label("loc_477")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05Did you know? Ein's name was originally translated as 'Anne' in the novel\x01",
            "Carnelia, but this name dropped the meaning to her name, which is 'One'\x01",
            "in German. That's why it's respectfully back to 'Ein' now.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xF2, 0x0)

    label("loc_567")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_39E end

    def Function_4_575(): pass

    label("Function_4_575")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x575, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x204, 1)"), scpexpr(EXPR_END)), "loc_5E3")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05Found \x1F\x04\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BAA)
    Jump("loc_64B")

    label("loc_5E3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05Found \x1F\x04\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x04\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_64B")

    Jump("loc_6D8")

    label("loc_64E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x05(11/12) Ding-dong!\x01",
            "The cheap chime of her door-bell echoed through the empty apartment.\x01",
            "'Who's there?'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xF3, 0x0)

    label("loc_6D8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_575 end

    def Function_5_6E6(): pass

    label("Function_5_6E6")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05Open the Door?\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_5_6E6 end

    def Function_6_73F(): pass

    label("Function_6_73F")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, 22200, 5000, 30930, 0)
    SetChrPos(0x1, 23820, 5000, 30870, 0)
    SetChrPos(0x2, 22220, 5000, 29200, 0)
    SetChrPos(0x3, 23780, 5000, 29000, 0)
    OP_6D(23130, 5000, 31450, 0)
    OP_67(0, 5480, -10000, 0)
    OP_6B(3880, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_815")
    OP_28(0x6, 0x4, 0x2)
    OP_82(0x81, 0x2)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_815")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #10
        (
            "\x07\x05#40WHappiness comes in many forms and\x01",
            "can be interpreted in many ways.\x01",
            "#500W \x01",
            "#40WPresent to me a form of happiness you\x01",
            "have obtained.\x01",
            "Only then shall the door open...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x2D9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_91F")
    Call(0, 5)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91C")
    Call(0, 7)

    label("loc_91C")

    Jump("loc_91F")

    label("loc_91F")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_6_73F end

    def Function_7_92B(): pass

    label("Function_7_92B")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x5)
    Sleep(500)

    def lambda_994():
        OP_6B(3100, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_994)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_E3(0x0, 0x9, 0, 0x0)
    NewScene("ED6_DT21/P9000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_92B end

    def Function_8_9E1(): pass

    label("Function_8_9E1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, 22200, 5000, 30930, 0)
    SetChrPos(0x1, 23820, 5000, 30870, 0)
    SetChrPos(0x2, 22220, 5000, 29200, 0)
    SetChrPos(0x3, 23780, 5000, 29000, 0)
    OP_6D(23130, 5000, 31450, 0)
    OP_67(0, 5480, -10000, 0)
    OP_6B(3880, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_8_9E1 end

    SaveToFile()

Try(main)
