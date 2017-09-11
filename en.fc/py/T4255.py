from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4255   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4255.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        'Shea',                                 # 9
        'Head Cook Gervais',                    # 10
        'Folk',                                 # 11
        'Regis',                                # 12
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
        'ED6_DT07/CH02460 ._CH',             # 00
        'ED6_DT07/CH02230 ._CH',             # 01
        'ED6_DT07/CH02240 ._CH',             # 02
        'ED6_DT07/CH02540 ._CH',             # 03
        'ED6_DT07/CH01280 ._CH',             # 04
        'ED6_DT07/CH01520 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH02460P._CP',             # 00
        'ED6_DT07/CH02230P._CP',             # 01
        'ED6_DT07/CH02240P._CP',             # 02
        'ED6_DT07/CH02540P._CP',             # 03
        'ED6_DT07/CH01280P._CP',             # 04
        'ED6_DT07/CH01520P._CP',             # 05
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -68800,
        Z                   = 0,
        Y                   = 73190,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -62700,
        Z                   = 0,
        Y                   = 67500,
        Direction           = 258,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -71490,
        Z                   = 0,
        Y                   = 65550,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    ScpFunction(
        "Function_0_15A",          # 00, 0
        "Function_1_20F",          # 01, 1
        "Function_2_229",          # 02, 2
        "Function_3_3A6",          # 03, 3
        "Function_4_649",          # 04, 4
        "Function_5_7BF",          # 05, 5
        "Function_6_BC7",          # 06, 6
    )


    def Function_0_15A(): pass

    label("Function_0_15A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_184")
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 1)
    SetChrChipByIndex(0x138, 2)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_184")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_1C6")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -68800, 0, 72170, 273)
    OP_43(0x8, 0x0, 0x0, 0x2)
    SetChrPos(0x9, -61660, 0, 68120, 76)
    Jump("loc_20E")

    label("loc_1C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1D0")
    Jump("loc_20E")

    label("loc_1D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_1E9")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_20E")

    label("loc_1E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_1FD")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_20E")

    label("loc_1FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_207")
    Jump("loc_20E")

    label("loc_207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_20E")

    label("loc_20E")

    Return()

    # Function_0_15A end

    def Function_1_20F(): pass

    label("Function_1_20F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_END)), "loc_21F")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_21F")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_20F end

    def Function_2_229(): pass

    label("Function_2_229")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24E")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_390")

    label("loc_24E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_267")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_390")

    label("loc_267")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_280")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_390")

    label("loc_280")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_299")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_390")

    label("loc_299")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B2")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_390")

    label("loc_2B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CB")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_390")

    label("loc_2CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E4")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_390")

    label("loc_2E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FD")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_390")

    label("loc_2FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_316")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_390")

    label("loc_316")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32F")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_390")

    label("loc_32F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_348")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_390")

    label("loc_348")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_361")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_390")

    label("loc_361")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37A")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_390")

    label("loc_37A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_390")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_390")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A5")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_390")

    label("loc_3A5")

    Return()

    # Function_2_229 end

    def Function_3_3A6(): pass

    label("Function_3_3A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_3B3")
    Jump("loc_645")

    label("loc_3B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_408")

    ChrTalk(    #0
        0xFE,
        "A coup d'etat AND rats?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "Damn that Intelligence Division!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BE")

    label("loc_408")

    OP_A2(0x3)

    ChrTalk(    #2
        0xFE,
        (
            "I found out where the rats were\x01",
            "coming from.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Seems they've been breeding in\x01",
            "the castle's treasury...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "A coup d'etat AND rats?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "Damn that Intelligence Division!\x02",
    )

    CloseMessageWindow()

    label("loc_4BE")

    Jump("loc_645")

    label("loc_4C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_4CB")
    Jump("loc_645")

    label("loc_4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_4D5")
    Jump("loc_645")

    label("loc_4D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_584")

    ChrTalk(    #6
        0xFE,
        (
            "I've got be careful how I store\x01",
            "the food, so those damned rats\x01",
            "don't get in it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "...Which reminds me, do rats\x01",
            "really like cheese, or is that\x01",
            "just a myth?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_645")

    label("loc_584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_645")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5C0")

    ChrTalk(    #8
        0xFE,
        (
            "Where are these rats all coming\x01",
            "from?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_645")

    label("loc_5C0")

    OP_A2(0x3)

    ChrTalk(    #9
        0xFE,
        (
            "The rat problem around here is\x01",
            "starting to get out of control.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "I can't stand rats, either, so\x01",
            "this really sucks for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_645")

    TalkEnd(0xFE)
    Return()

    # Function_3_3A6 end

    def Function_4_649(): pass

    label("Function_4_649")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_656")
    Jump("loc_7BB")

    label("loc_656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_6D7")

    ChrTalk(    #11
        0xFE,
        "Vegetable dishes are my specialty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "After all...I'm a Rolent man!\x01",
            "And vegetables are what real\x01",
            "Rolent men do!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BB")

    label("loc_6D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_6E1")
    Jump("loc_7BB")

    label("loc_6E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_6EB")
    Jump("loc_7BB")

    label("loc_6EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_731")

    ChrTalk(    #13
        0xFE,
        (
            "*sigh* I just want to clean up\x01",
            "here and get back home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BB")

    label("loc_731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_7BB")

    ChrTalk(    #14
        0xFE,
        (
            "The head chef is a real pro, specializing\x01",
            "in imperial cuisine...over one thousand\x01",
            "dishes of it, in fact. He's simply amazing!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BB")

    TalkEnd(0xFE)
    Return()

    # Function_4_649 end

    def Function_5_7BF(): pass

    label("Function_5_7BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_835")

    ChrTalk(    #15
        0xFE,
        (
            "Broth, onions, celery, carrots,\x01",
            "laurel and har--er, parsley...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "I'm making tomorrow's bouillon.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BC3")

    label("loc_835")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_897")

    ChrTalk(    #17
        0xFE,
        (
            "When Her Majesty and the princess\x01",
            "dine together, THAT'S when I feel\x01",
            "real pressure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BC3")

    label("loc_897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_8A1")
    Jump("loc_BC3")

    label("loc_8A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_9EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_901")

    ChrTalk(    #18
        0xFE,
        (
            "And right now, Her Majesty needs\x01",
            "nutrients--so the pressure is\x01",
            "SURELY on!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9EB")

    label("loc_901")

    OP_A2(0x1)

    ChrTalk(    #19
        0xFE,
        "Ah, Hilda!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "I wanted to talk to you about\x01",
            "Her Majesty's diet.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #21
        0x0,
        "Head Maid Hilda",
        (
            "#710FBut I can't right now... I'm\x01",
            "in the middle of several things\x01",
            "at once.\x02\x03",

            "Later, though, we must sit down\x01",
            "and talk. If you'd be so kind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9EB")

    Jump("loc_BC3")

    label("loc_9EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_A2E")

    ChrTalk(    #22
        0xFE,
        "Ah, hello, hello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "Did you enjoy my cuisine?\x02",
    )

    CloseMessageWindow()
    Jump("loc_BC3")

    label("loc_A2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_BC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B2E")

    ChrTalk(    #24
        0xFE,
        (
            "Ah, I'm sorry, but we're not\x01",
            "ready for you yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "I'm afraid we're still preparing\x01",
            "dinner at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "Once it's done, though, we'll make\x01",
            "sure everyone knows. And until then,\x01",
            "your patience is greatly appreciated.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BC3")

    label("loc_B2E")


    ChrTalk(    #27
        0xFE,
        "The main course...is complete!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "Once dinner is ready, we'll make sure\x01",
            "everyone knows. And until then, your\x01",
            "patience is greatly appreciated.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC3")

    TalkEnd(0xFE)
    Return()

    # Function_5_7BF end

    def Function_6_BC7(): pass

    label("Function_6_BC7")

    TalkBegin(0xFE)

    ChrTalk(    #29
        0xFE,
        "Joshua?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "I'm afraid I haven't seen him...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_BC7 end

    SaveToFile()

Try(main)
