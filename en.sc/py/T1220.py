from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1220   ._SN',
        MapName             = 'Bose',
        Location            = 'T1220.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        'Emile',                                # 9
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


    AddCharChip(
        'ED6_DT07/CH01040 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01040P._CP',             # 00
    )

    DeclNpc(
        X                   = -1600,
        Z                   = -1000,
        Y                   = 7600,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    DeclActor(
        TriggerX            = -670,
        TriggerZ            = -1000,
        TriggerY            = 6680,
        TriggerRange        = 400,
        ActorX              = -1600,
        ActorZ              = 500,
        ActorY              = 7600,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_F6",           # 00, 0
        "Function_1_F7",           # 01, 1
        "Function_2_155",          # 02, 2
        "Function_3_16B",          # 03, 3
        "Function_4_1E1",          # 04, 4
    )


    def Function_0_F6(): pass

    label("Function_0_F6")

    Return()

    # Function_0_F6 end

    def Function_1_F7(): pass

    label("Function_1_F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_10A")
    OP_B1("T1220_n")
    Jump("loc_126")

    label("loc_10A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_11D")
    OP_B1("T1220_y")
    Jump("loc_126")

    label("loc_11D")

    OP_B1("T1220_n")

    label("loc_126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_137")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_137")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_147")
    OP_10(0x0, 0x0)
    OP_10(0x2, 0x1)
    Jump("loc_154")

    label("loc_147")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_154")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)

    label("loc_154")

    Return()

    # Function_1_F7 end

    def Function_2_155(): pass

    label("Function_2_155")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_16A")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_155")

    label("loc_16A")

    Return()

    # Function_2_155 end

    def Function_3_16B(): pass

    label("Function_3_16B")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CB")
    OP_0D()
    OP_A9(0x46)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_1CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DC")
    TalkEnd(0x8)
    Return()

    label("loc_1DC")

    Call(0, 4)
    Return()

    # Function_3_16B end

    def Function_4_1E1(): pass

    label("Function_4_1E1")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_359")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CF")

    ChrTalk(    #0
        0x8,
        (
            "I guess the airships and freight\x01",
            "caravans still aren't running.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "Most of our goods are shipped in\x01",
            "from Bose, so...that sucks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        "Not much WE can do about it, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        "*sigh* All I got now are sighs!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_356")

    label("loc_2CF")


    ChrTalk(    #4
        0x8,
        (
            "Most of our goods are shipped in\x01",
            "from Bose, so...that sucks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "With all the shipping stopped, I'm\x01",
            "gonna run out of stock soon!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_356")

    Jump("loc_922")

    label("loc_359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_52E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_464")

    ChrTalk(    #6
        0x8,
        "Hey, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "For the moment, I'm still in business.\x01",
            "Somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "Seems that the orbments have stopped\x01",
            "working in Bose, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "With the freight caravans not running,\x01",
            "I'm gonna run out of stuff to sell!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        "*sigh* What should I do?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_52B")

    label("loc_464")


    ChrTalk(    #11
        0x8,
        (
            "For the moment, I'm still in business.\x01",
            "Somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "Seems that the orbments have stopped\x01",
            "working in Bose, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "Bad as it is here, I can't imagine\x01",
            "what it's like in a big city like Bose...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52B")

    Jump("loc_922")

    label("loc_52E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_5C7")

    ChrTalk(    #14
        0x8,
        "We're getting donations from all over.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        "It really warms the heart!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "It feels like the cheer's finally coming\x01",
            "back to the village.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_922")

    label("loc_5C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_68E")

    ChrTalk(    #17
        0x8,
        (
            "The clean-up of the orchards is going\x01",
            "forward as planned, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        "I wonder how the talks went.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "If we don't work together, restoring the\x01",
            "orchards'll be a dream within a dream.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_922")

    label("loc_68E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_814")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_727")

    ChrTalk(    #20
        0x8,
        (
            "Any time I see an army uniform...\x01",
            "I still get a twinge of anxiety, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "The days of the war always come\x01",
            "flooding back...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_811")

    label("loc_727")


    ChrTalk(    #22
        0x8,
        (
            "Looks like the Royal Army soldiers have\x01",
            "pulled out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "I feel terrible for saying this, but...\x01",
            "any time I see an army uniform, I still\x01",
            "get a twinge of anxiety, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "The days of the war always come\x01",
            "flooding back...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_811")

    Jump("loc_922")

    label("loc_814")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_922")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_883")

    ChrTalk(    #25
        0x8,
        "The damage to the orchards is...terrible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        "We won't be harvesting a thing this year.\x02",
    )

    CloseMessageWindow()
    Jump("loc_922")

    label("loc_883")


    ChrTalk(    #27
        0x8,
        "Hey, welcome...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "The fires may be out, but the damage to\x01",
            "the orchards is... It's just terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "I wonder if Ravennue can even\x01",
            "survive this...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_922")

    TalkEnd(0x8)
    Return()

    # Function_4_1E1 end

    SaveToFile()

Try(main)
